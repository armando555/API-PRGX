from tests.base import client
from schema.address import AddressSchema
from repository.address import create as address_create


class TestGetByIdAddress:
    def test_get_by_id_address(self, db):
        address_create(db=db,request=AddressSchema(address_1="address.address_1", address_2="address.address_2", city="address.city", state="address.state", country="address.country", zip="address.zip"))
        response = client.get(
            "/address/1",
        )

        assert response.status_code == 200
        assert response.json()["address_1"] == "address.address_1"
        assert response.json()["address_2"] == "address.address_2"