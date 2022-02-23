import requests


class GUI_Helper:

    default_config_params = {"max_retries": 5,
                             "show_timeout": 1,
                             "url": "http://localhost:8000"}

    default_keys_set = set(default_config_params.keys())

    def __init__(self, **config_params):
        super().__init__()
        print(f"Using default value for {self.default_keys_set}")
        for config_key in self.default_keys_set:
            setattr(self, config_key,
                    self.default_config_params[config_key])

    def send_request(self, method, route, params=None, data=None):
        full_uri = ''.join([self.url, route])
        response = requests.request(method=method, url=full_uri,
                                    params=params, json=data)
        return response