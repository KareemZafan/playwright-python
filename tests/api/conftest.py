# tests/api/conftest.py
import pytest
from playwright.sync_api import Playwright

BASE_URL = "https://restful-booker.herokuapp.com"

@pytest.fixture(scope="session")
def api_context(playwright: Playwright):
    ctx = playwright.request.new_context(base_url=BASE_URL)
    yield ctx
    ctx.dispose()

@pytest.fixture(scope="session")
def auth_token(api_context):
    r = api_context.post("/auth",
            data={"username": "admin", "password": "password123"})
    assert r.status == 200
    return r.json()["token"]

@pytest.fixture
def created_booking_id(api_context):
    r = api_context.post("/booking", data={
        "firstname": "Test", "lastname": "User",
        "totalprice": 100, "depositpaid": True,
        "bookingdates": {"checkin": "2024-06-01",
                          "checkout": "2024-06-03"},
        "additionalneeds": ""
    })
    booking_id = r.json()["bookingid"]
    yield booking_id
    # Teardown: clean up
    api_context.delete(f"/booking/{booking_id}")
