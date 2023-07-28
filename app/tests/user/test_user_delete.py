from tests.base import client
from schema.user import UserSchema
from repository.user import create as user_create


class TestDeleteUser:
    def test_delete_user(self, db):
        user_create(db=db,request=UserSchema(first_name="Jesus",last_name="Cristo",email="oli@asd.com",password="jesus123."))
        response = client.delete(
            "/user/1",
        )

        assert response.status_code == 204