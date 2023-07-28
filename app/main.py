from fastapi import FastAPI
from routers import user_router, address_router
from database.engine import engine
import config
from models.base import init
from sqladmin import Admin
from views import *



app = FastAPI(title=config.title)
admin = Admin(app, engine)

admin.add_view(UserAdmin)
admin.add_view(AddressAdmin)

app.include_router(user_router)
app.include_router(address_router)


#Initialize Data Model
init()