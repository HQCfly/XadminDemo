from django.db import models

from Xadmin.service.Xadmin import site,ModelXadmin

from app02.models import *

site.register(Transactions)


class FoodeatConfig(ModelXadmin):
    list_display = ["id","title"]
site.register(Foodeat,FoodeatConfig)

print("_registry",site._registry)

