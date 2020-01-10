from django.contrib import admin
from . import models

admin.site.register([
    models.Goods,
    models.OrderClient,
    models.Transport,
    models.TransportFull,
    models.GoodsCount,
    models.Driver,
    models.Address,

    ])
