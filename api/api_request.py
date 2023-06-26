import allure
import requests


class ApiRequest:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()

    @allure.step("GET: {url}")
    def get(self, url: str, **kwargs: dict) -> requests.Response:
        response = self.session.get(f"{self.base_url}/{url}", **kwargs)
        allure.attach(response.url, "Request url", allure.attachment_type.JSON)
        allure.attach(
            response.text,
            f"Response: {response.status_code}:{response.reason}",
            allure.attachment_type.JSON,
        )
        return response

    @allure.step("POST: {url}")
    def post(self, url: str, **kwargs: dict) -> requests.Response:
        response = self.session.post(f"{self.base_url}/{url}", **kwargs)
        allure.attach(response.url, "Request url", allure.attachment_type.JSON)
        allure.attach(
            response.text,
            f"Response: {response.status_code}:{response.reason}",
            allure.attachment_type.JSON,
        )
        return response

    @allure.step("PUT: {url}")
    def put(self, url: str, **kwargs: dict) -> requests.Response:
        response = self.session.put(f"{self.base_url}/{url}", **kwargs)
        allure.attach(response.url, "Request url", allure.attachment_type.JSON)
        allure.attach(
            response.text,
            f"Response: {response.status_code}:{response.reason}",
            allure.attachment_type.JSON,
        )
        return response

    @allure.step("DELETE: {url}")
    def delete(self, url: str, **kwargs: dict) -> requests.Response:
        response = self.session.delete(f"{self.base_url}/{url}", **kwargs)
        allure.attach(response.url, "Request url", allure.attachment_type.JSON)
        allure.attach(
            response.text,
            f"Response: {response.status_code}:{response.reason}",
            allure.attachment_type.JSON,
        )
        return response

    @allure.step("PATCH: {url}")
    def patch(self, url: str, **kwargs: dict) -> requests.Response:
        response = self.session.patch(f"{self.base_url}/{url}", **kwargs)
        allure.attach(response.url, "Request url", allure.attachment_type.JSON)
        allure.attach(
            response.text,
            f"Response: {response.status_code}:{response.reason}",
            allure.attachment_type.JSON,
        )
        return response
