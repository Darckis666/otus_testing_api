import pytest
import requests
import json

base_url = ''
uath = '/api/authentication/authenticate'


def test_auth_page():
    r = requests.get("https://test.tis24.kz")
    assert r.status_code == 200
    # asser r.text['title']=='Trinity'


@pytest.mark.parametrize("login, password, rezult", [('test@mail.ru', 'Qwerty1!', False)])
def test_authorize(login, password, rezult):
    response = requests.post(base_url + uath, json.dumps({"login": login, "password": password}))
    assert response.status_code == 200
    # if (rezult):
    #     response.json()
    # else:
    #     assert response.json()['error']['code']==1
