from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)


def test_get_users():
    response = client.get("/users")
    assert response.status_code == 200


def test_get_user_by_email():
    email = 'Sincere@april.biz'
    response = client.get(f"/users/{email}")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Leanne Graham", "username": "Bret", "email": "Sincere@april.biz",
                               "address": {"street": "Kulas Light", "suite": "Apt. 556", "city": "Gwenborough",
                                           "zipcode": "92998-3874", "geo": {"lat": "-37.3159", "lng": "81.1496"}},
                               "phone": "1-770-736-8031 x56442", "website": "hildegard.org",
                               "company": {"name": "Romaguera-Crona",
                                           "catchPhrase": "Multi-layered client-server neural-net",
                                           "bs": "harness real-time e-markets"}}


def test_get_not_existing_user_by_email():
    email = 'testerror@gmail.com'
    response = client.get(f"/users/{email}")
    assert response.status_code == 404
