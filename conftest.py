import pytest
import requests


@pytest.fixture()
def base_url():
    yield "http://pulse-rest-testing.herokuapp.com/"


@pytest.fixture(scope="module")
def session():
    return requests.Session()


@pytest.fixture(scope="session")
def token(base_url):
    r_token = requests.post(f'{base_url}/api-token-auth/',
                            data={'username': 'admin', 'password': 'pass'})
    token = r_token.json()['token']
    return token


@pytest.fixture()
def book(base_url):
    book_data = {"title": "New", "author": "New"}
    resp = requests.post(f'{base_url}/books', data=book_data)
    book_body_resp = resp.json()
    yield book_body_resp
    resp = requests.delete(f'{base_url}/books/{book_body_resp["id"]}')
    # print(resp.status_code)


@pytest.fixture()
def delete_role(base_url):
    d = {}
    yield d
    if "id" in d:
        requests.delete(f'{base_url}/roles/{d["id"]}')

role_payload_list =[
    {
        "name": "Polonius",
        "type": "Secondary",
        "level": 100,
    },
    {
        "name": "#@$#$%^",
        "type": "%$^&*(",
        "level": 2,
    },
    {
        "name": "23456789",
        "type": "345678",
        "level": 2,
    }
]


@pytest.fixture(params=role_payload_list, ids=[str(data) for data in role_payload_list])
def role_payload(request):
    return request.param
