from requests import Response

from api.api_request import ApiRequest
from utils.utils import to_dict


class ApiOpenAi:

    def __init__(self, api: ApiRequest, openai_api_key: str):
        self.api = api
        self.api.session.headers.update({"Content-Type": "application/json"})
        self.api.session.headers.update({"Authorization": f"Bearer {openai_api_key}"})

    def get_models(self) -> Response:
        return self.api.get("models")

    def get_model(self, model_id) -> Response:
        return self.api.get(f"models/{model_id}")

    def create_completion(self, completion) -> Response:
        return self.api.post(
            "completions",
            json=to_dict(completion)
        )

