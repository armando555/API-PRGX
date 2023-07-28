from tests.base import client
from schema.user import UserSchema
from repository.user import bulk as user_bulk
from schema.address import AddressSchema
from repository.address import bulk as address_bulk


class TestGetUserByCountry:
    def test_get_user_by_country(self, db):
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
                UserSchema(
                    first_name="Jesus3",
                    last_name="Cristo4",
                    email="oli4@asd.com",
                    password="jesus51253.",
                ),
            ],
        )
        address_bulk(
            db=db,
            request=[
                AddressSchema(
                    address_1="address_1",
                    address_2="address_2",
                    city="city",
                    state="state",
                    country="country",
                    zip="zip",
                    user_id_fk=1
                ),
                AddressSchema(
                    address_1="address_1",
                    address_2="address_2",
                    city="city",
                    state="state",
                    country="country",
                    zip="zip",
                    user_id_fk=3
                ),
                AddressSchema(
                    address_1="address_1",
                    address_2="address_2",
                    city="city",
                    state="state",
                    country="country2",
                    zip="zip",
                    user_id_fk=2
                ),
                AddressSchema(
                    address_1="address_1",
                    address_2="address_2",
                    city="city",
                    state="state",
                    country="country3",
                    zip="zip",
                    user_id_fk=1
                ),
            ],
        )
        response = client.get(
            "/user/by_country?country=country",
        )

        assert response.status_code == 200
        assert response.json()[0]["first_name"] == "Jesus"
