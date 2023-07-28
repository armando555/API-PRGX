from tests.base import client
from schema.user import UserSchema
from repository.user import create as user_create


class TestUpdateUser:
    def test_update_user(self, db):
        user_create(db=db,request=UserSchema(first_name="Jesus",last_name="Cristo",email="oli@asd.com",password="jesus123."))
        response = client.put(
            "/user/1",
            json={"first_name": "Jesuscrito", "last_name": "Cristo","email":"oli@asd.com","password":"jesus123."},
        )

        assert response.status_code == 202