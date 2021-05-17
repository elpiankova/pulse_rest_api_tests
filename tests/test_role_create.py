import sys

import pytest
import requests


# pytestmark = pytest.mark.skipif(sys.platform.startswith("win"), reason="Not at Windows platform")

# @pytest.mark.xfail(strict=True)

# def test_create_role(book, base_url, role_payload):
#     pass

def test_create_role(delete_role, book, base_url, role_payload):
    role_payload["book"] = book["id"]
    resp = requests.post(f'{base_url}/roles', data=role_payload)
    assert resp.status_code == 201
    resp_body = resp.json()
    assert "id" in resp_body
    delete_role.update(resp_body)
    for key in role_payload:
        assert resp_body[key] == role_payload[key]

