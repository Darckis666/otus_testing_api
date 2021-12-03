import pytest
import requests


class APIClient:

    def __init__(self, base_adress):
        self.base_adress = base_adress

    def post(self, path="/", params=None, data=None, headers=None):
        url = self.base_adress + path
        return requests.post(url=url, params=params, data=data, headers=headers)

    def get(self, path="/", params=None):
        return requests.get(url=self.base_adress + path, params=params)


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default="https://ya.ru",
        help="This is request url"
    )


@pytest.fixture(scope="session")
def api_client(request):
    base_url = request.config.getoption("--url")
    return APIClient(base_adress=base_url)
