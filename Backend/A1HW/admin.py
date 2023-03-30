from django.contrib import admin
from .models import Car, CarBrand, Owner,CarWorkshop,CarTunedBy

admin.site.register(Car)
admin.site.register(CarBrand)
admin.site.register(Owner)
admin.site.register(CarWorkshop)
admin.site.register(CarTunedBy)