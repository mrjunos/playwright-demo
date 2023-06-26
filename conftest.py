import pytest

from api.api_openai import ApiOpenAi
from api.api_request import ApiRequest
from utils import consts


@pytest.fixture(scope="session")
def creds(test_env):
    return consts.creds(test_env)


@pytest.fixture(scope="session")
def api(creds):
    api = ApiRequest(creds["url"])
    return ApiOpenAi(api, creds["openai_api_key"])
