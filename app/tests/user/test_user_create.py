from tests.base import client


class TestCreateUser:
    def test_create_user(self, db):
        response = client.post(
            "/user/",
            json={
                "first_name": "Jesus",
                "last_name": "Cristo",
                "email": "cristo@gmail.com",
                "password": "Cristo123.",
            },
        )
        assert response.status_code == 201
        assert response.json()["first_name"] == "Jesus"
        assert response.json()["last_name"] == "Cristo"
