from tests.base import client
from schema.user import UserSchema
from repository.user import create as user_create


class TestGetByIdUser:
    def test_get_by_id_user(self, db):
        user_create(db=db,request=UserSchema(first_name="Jesus",last_name="Cristo",email="oli@asd.com",password="jesus123."))
        response = client.get(
            "/user/1",
        )

        assert response.status_code == 200
        assert response.json()["first_name"] == "Jesus"
        assert response.json()["last_name"] == "Cristo"