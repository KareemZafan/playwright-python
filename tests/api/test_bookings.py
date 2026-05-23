# Create a booking
def test_create_booking(api_context):
    ## JSON payload for creating a booking
    payload = {
        "firstname": "Kareem",
        "lastname":  "Mohamed",
        "totalprice": 2000,
        "depositpaid": True,
        "bookingdates": {
            "checkin":  "2026-06-01",
            "checkout": "2026-06-07"
        },
        "additionalneeds": "Breakfast"
    }
    response = api_context.post("/booking",
                                data=payload)
    assert response.status == 200
    body = response.json()
    assert "bookingid" in body
    assert "bookingid" != None
    assert body["booking"]["firstname"] == "Kareem"
    assert body["booking"]["lastname"] == "Mohamed"
    assert body["booking"]["totalprice"] == 2000
    assert body["booking"]["depositpaid"] is True
    


# List all bookings
def test_get_all_bookings(api_context):
    response = api_context.get("/booking") ## BASE_URL + "/booking"
    assert response.status == 200
    bookings = response.json()
    assert isinstance(bookings, list)
    assert len(bookings) > 0

# Get single booking
def test_get_booking_by_id(api_context,
                           created_booking_id):
    r = api_context.get(
            f"/booking/{created_booking_id}")
    assert r.status == 200
    body = r.json()
    assert "firstname" in body
    assert "bookingdates" in body
    assert body["depositpaid"] in [True, False]


# Full update  PUT (requires auth token)
def test_update_booking(api_context, auth_token,
                        created_booking_id):
    headers = {"Cookie": f"token={auth_token}"}
    payload = {
        "firstname": "Alice", "lastname": "Smith",
        "totalprice": 399,    "depositpaid": True,
        "bookingdates": {"checkin":  "2024-05-01",
                          "checkout": "2024-05-05"},
        "additionalneeds": "Late checkout"
    }
    r = api_context.put(
            f"/booking/{created_booking_id}",
            headers=headers, data=payload)
    assert r.status == 200
    assert r.json()["firstname"] == "Alice"
    assert r.json()["lastname"] == "Smith"
    assert r.json()["additionalneeds"] == "Late checkout"
    


# Partial update  PATCH
def test_partial_update(api_context, auth_token,
                        created_booking_id):
    headers = {"Cookie": f"token={auth_token}"}
    r = api_context.patch(
            f"/booking/{created_booking_id}",
            headers=headers,
            data={"totalprice": 5000})
    assert r.status == 200
    assert r.json()["totalprice"] == 5000

# Delete booking
def test_delete_booking(api_context, auth_token,
                        created_booking_id):
    headers = {"Cookie": f"token={auth_token}"}
    r = api_context.delete(
            f"/booking/{created_booking_id}",
            headers=headers)
    assert r.status == 201   # 201 = Deleted
    # Verify deletion
    r = api_context.get(f"/booking/{created_booking_id}")
    assert r.status == 404   # 404 = Not Found
