from tests.base import client
from schema.address import AddressSchema
from repository.address import bulk as address_bulk


class TestGetAddress:
    def test_get_address(self, db):
        address_bulk(
            db=db,
            request=[
                AddressSchema(
                    address_1="address.address_1",
                    address_2="address.address_2",
                    city="address.city",
                    state="address.state",
                    country="address.country",
                    zip="address.zip",
                ),
                AddressSchema(
                    address_1="address.address_1",
                    address_2="address.address_2",
                    city="address.city",
                    state="address.state",
                    country="address.country",
                    zip="address.zip",
                ),
            ],
        )
        response = client.get(
            "/address/",
        )

        assert response.status_code == 200
