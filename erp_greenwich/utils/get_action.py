import ast


def get_api_actions() -> dict:
    from rest_framework.routers import SimpleRouter

    from config import api_router
    from erp_greenwich.auth.oauth2_config.permissions.token_with_action import (
        IsAuthenticatedOrTokenPermissionWithAction,
    )

    registry = api_router.router.registry
    res_dict = {r[1].__name__: r[2] for r in registry}
    api_actions = []
    labels = []
    for res in registry:
        if IsAuthenticatedOrTokenPermissionWithAction in res[1].permission_classes:
            router = SimpleRouter()
            routes = router.get_routes(res[1])
            action_list = []
            for route in routes:
                action_list += list(route.mapping.values())
            distinct_action_list = list(set(action_list))
            distinct_action_list.remove("partial_update")
            basename = res_dict.get(res[1].__name__)
            labels.append(str(basename).title())
            api_actions.extend(
                [f"{basename}:{action}" for action in distinct_action_list]
            )
    api_actions = list(set(api_actions))
    labels = list(set(labels))
    context = {"scopes": api_actions, "labels": labels}
    return context


def read_file_json(file_path: str) -> dict:
    """
    Read file.json and return a dict of data
    """
    import json

    with open(file_path, "r") as json_file:
        data: dict = json.load(json_file)
    return data


def convert_string_array_to_list(array_string) -> list:
    list_convert = ast.literal_eval(array_string)
    list_convert = [n.strip() for n in list_convert]
    return list_convert


def convert_list_string_to_space(list_return) -> str:
    list_to_str = " ".join(map(str, list_return))
    return list_to_str


def convert_array_to_dict(array_key, array_value) -> dict:
    array_key = list(set(array_key))
    array_value = list(set(array_value))
    dict_return = dict(zip(array_key, array_value))
    return dict_return
