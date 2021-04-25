import requests


def test_create_role(book, base_url):
    role_data = {
        "name": "Polonius",
        "type": "Secondary",
        "level": 2,
        "book": book["id"]
    }
    resp = requests.post(f'{base_url}/roles', data=role_data)
    assert resp.status_code == 201
    resp_body = resp.json()
    assert "id" in resp_body
    for key in role_data:
        assert resp_body[key] == role_data[key]

