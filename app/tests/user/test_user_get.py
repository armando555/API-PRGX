from tests.base import client
from schema.user import UserSchema
from repository.user import bulk as user_bulk


class TestGetUser:
    def test_get_user(self, db):
        user_bulk(
            db=db,
            request=[
                UserSchema(
                    first_name="Jesus",
                    last_name="Cristo",
                    email="oli@asd.com",
                    password="jesus123.",
                ),
                UserSchema(
                    first_name="Jesus2",
                    last_name="Cristo3",
                    email="oli2@asd.com",
                    password="jesus5123.",
                ),
            ],
        )
        response = client.get(
            "/user/",
        )

        assert response.status_code == 200
