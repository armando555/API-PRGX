from tests.base import client
from schema.address import AddressSchema
from repository.address import create as address_create


class TestUpdateAddress:
    def test_update_address(self, db):
        address_create(db=db,request=AddressSchema(address_1="Jesuscrito", address_2="Cristo", city="address.city", state="address.state", country="address.country", zip="address.zip"))
        response = client.put(
            "/address/1",
            json={"address_1": "Jesuscrito2", "address_2": "Cristo2","city":"address.city2","state":"address.state2","country":"address.country2","zip":"jeje"},
        )

        assert response.status_code == 202