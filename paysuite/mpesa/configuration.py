class Configuration:
    PARAMS = [
        'user_agent',
        'api_key',
        'public_key',
        'timeout',
        'verify_ssl',
        'debugging',
        'access_token',
        'environment'
    ]

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if key in self.PARAMS:
                self.__dict__[key] = value

    def build_default_operations(self)
        pass

    def build_default_headers(self):
        pass

    def generate_headers(self):
        pass

    def generate_authorization_header(self):
        pass

    def generate_url(self, operation):
        pass

    def is_valid(self):
        pass

    def generate_base_url(self, operation):
        pass
