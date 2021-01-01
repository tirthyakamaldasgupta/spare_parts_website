from django.shortcuts import render
from .models import CarManufacturers, CarSeries, PartsCategories, Items
from .serializers import CarManufacturersSerializer, CarseriesSerializer, PartsCategoriesSerializer, AllItemsSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

# API showing the details of car manufacturers
def viewCarManufacturers(request):
    car_manufacturers_objects = CarManufacturers.objects.all()
    serialized_car_manufacturers_objects = CarManufacturersSerializer(car_manufacturers_objects, many=True)
    jsoned_car_manufacturers_objects = JSONRenderer().render(serialized_car_manufacturers_objects.data)
    return HttpResponse(jsoned_car_manufacturers_objects)

#API showing the model lines/series produced by a car manufacturer
def viewCarSeries(request, pk):
    car_manufacturer_object = CarManufacturers.objects.get(pk = pk)
    car_series_objects = car_manufacturer_object.carseries_set.all()
    serialized_car_series_objects = CarseriesSerializer(car_series_objects, many=True)
    jsoned_car_series_objects = JSONRenderer().render(serialized_car_series_objects.data)
    return HttpResponse(jsoned_car_series_objects)

# API showing the details of parts categories
def viewPartsCategories(request):
    parts_categories_objects = PartsCategories.objects.all()
    serialized_parts_categories_objects = PartsCategoriesSerializer(parts_categories_objects, many=True)
    jsoned_parts_categories_objects = JSONRenderer().render(serialized_parts_categories_objects.data)
    return HttpResponse(jsoned_parts_categories_objects)

#API showing the all the items coming under each category irrespective of specific series(s) of a car manufacturer
def viewAllItems(request, pk):
    category_object = PartsCategories.objects.get(pk = pk)
    categorized_items_objects = category_object.items_set.all()
    serialized_categorized_items_objects = AllItemsSerializer(categorized_items_objects, many=True)
    jsoned_categorized_items_objects = JSONRenderer().render(serialized_categorized_items_objects.data)
    return HttpResponse(jsoned_categorized_items_objects)