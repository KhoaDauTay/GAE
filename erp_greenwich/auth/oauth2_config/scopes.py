from django.conf import settings
from oauth2_provider.scopes import BaseScopes

from erp_greenwich.utils.get_action import read_file_json


class ScopesBackend(BaseScopes):
    def get_all_scopes(self):
        scopes_path = settings.SCOPES_JSON_PATH
        scopes: dict = read_file_json(scopes_path)
        return scopes

    def get_available_scopes(self, application=None, request=None, *args, **kwargs):
        # TODO: Get scopes in application
        scopes_path = settings.SCOPES_JSON_PATH
        scopes: dict = read_file_json(scopes_path)
        # return {"album:create": "Create object of Album"} # run success but can only use one scopes
        # return {'album:list', 'album:create'} # run success
        return list(scopes.keys())

    def get_default_scopes(self, application=None, request=None, *args, **kwargs):
        scopes_path = settings.SCOPES_JSON_PATH
        scopes: dict = read_file_json(scopes_path)
        return list(scopes.keys())
