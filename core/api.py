from ninja import NinjaAPI
from rota.api import rota_router


api = NinjaAPI()
api.add_router('', rota_router)