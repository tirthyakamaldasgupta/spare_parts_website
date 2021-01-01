from django.contrib import admin
from .models import CarManufacturers, CarSeries, PartsCategories, Items

# Register your models here.
admin.site.register(CarManufacturers)
admin.site.register(CarSeries)
admin.site.register(PartsCategories)
admin.site.register(Items)