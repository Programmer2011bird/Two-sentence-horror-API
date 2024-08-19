import requests


class API_controller:
    def __init__(self) -> None:
        self.URL = "http://127.0.0.1:8000/?content_type=new"

        self.RESPONSE = requests.get(self.URL)
        self.RESPONSE_JSON = self.RESPONSE.json()


if __name__ == "__main__":
    API = API_controller()
