from sqladmin import ModelView
from models.address import Address

class AddressAdmin(ModelView, model=Address):
    column_list = [Address.id, Address.address_1,Address.address_2,Address.user]