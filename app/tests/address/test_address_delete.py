from tests.base import client
from schema.address import AddressSchema
from repository.address import create as address_create


class TestDeleteAddress:
    def test_delete_address(self, db):
        address_create(
            db=db,
            request=AddressSchema(
                address_1="address.address_1",
                address_2="address.address_2",
                city="address.city",
                state="address.state",
                country="address.country",
                zip="address.zip",
            ),
        )
        response = client.delete(
            "/address/1",
        )

        assert response.status_code == 204
