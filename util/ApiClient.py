import requests

from entities.response_model import ResponseModel


class ApiClient:
    # TODO: атрибут URL нужно вынести в окружение
    """Это класс для обработки запросов"""
    __default_url = "https://opm-website.iot-asm-test1.insitech.live/api"

    def __init__(self, base_url = __default_url):
        self.base_url = base_url

    def get_search_results(self, query):
        """Получить объект из ответа api /search"""
        response = requests.get(f"{self.base_url}/search?text={query}")
        response.raise_for_status()
        return ResponseModel.model_validate(response.json())
