# from test_role_create import base_url
import pytest
import requests

# TODO get data from file
payload_list = [
    {'title': 'Son of the Wolf', 'author': 'Jack London'},
    {'title': '@#$%^&**(){}[]', 'author': '@#$%^&**(){}[]'},
    {'title': 'Кирилица', 'author': 'РПМОРИ'}
]

# ids_list = ['ascii letters', "spec symbols", "Cyrillic"]
# ids_list = (str(data) for data in payload_list)


@pytest.mark.parametrize("payload", payload_list, ids=(str(data) for data in payload_list))
def test_book_create(base_url, payload):
    resp = requests.post(f'{base_url}/books', data=payload)
    assert 'id' in resp.json()
    for key in payload:
        assert payload[key] == resp.json()[key]


@pytest.mark.parametrize("payload", payload_list, ids=(str(data) for data in payload_list))
def test_book_create2(base_url, payload):
    resp = requests.post(f'{base_url}/books', data=payload)
    assert 'id' in resp.json()
    for key in payload:
        assert payload[key] == resp.json()[key]