from oauth2_provider.scopes import BaseScopes


class ScopesBackend(BaseScopes):
    def get_all_scopes(self):
        pass

    def get_available_scopes(self, application=None, request=None, *args, **kwargs):
        # TODO: Get scopes in application
        # return {"album:create": "Create object of Album"} # run success but can only use one scopes
        # return {'album:list', 'album:create'} # run success
        pass

    def get_default_scopes(self, application=None, request=None, *args, **kwargs):
        pass
