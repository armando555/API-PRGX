from fastapi import FastAPI
from routers import bicycles_router
from database.engine import engine
import config
from models.base import init
from sqladmin import Admin
from views import *



app = FastAPI(title=config.title)
admin = Admin(app, engine)

admin.add_view(BicycleAdmin)

app.include_router(bicycles_router.router)


#Initialize Data Model
init()