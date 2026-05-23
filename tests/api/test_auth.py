# tests/api/test_auth.py
import pytest

def test_create_token_success(api_context):
    response = api_context.post("/auth", data={
        "username": "admin",
        "password": "password123"
    })
    assert response.status == 200
    body = response.json()
    assert "token" in body
    assert len(body["token"]) > 0
    print(f"Token: {body['token']}")


def test_invalid_password(api_context):
    response = api_context.post("/auth", data={
        "username": "admin",
        "password": "wrong"
    })
    assert response.status == 200
    body = response.json()
    assert body.get("reason") == "Bad credentials"


def test_invalid_username(api_context):
    response = api_context.post("/auth", data={
        "username": "wrong",
        "password": "password123"
    })
    assert response.status == 200
    body = response.json()
    assert body.get("reason") == "Bad credentials"