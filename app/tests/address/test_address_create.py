from tests.base import client


class TestCreateAddress:
    def test_create_address(self,db):
        response = client.post(
            "/address/",
            json={"address_1": "Jesus", "address_2": "Cristo", "city": "city2", "state": "asda.","zip": "asd", "country":"country1"},
        )
        assert response.status_code == 201
        assert response.json()["address_1"] == "Jesus"
        assert response.json()["address_2"] == "Cristo"