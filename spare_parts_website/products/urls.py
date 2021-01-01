from django.urls import path, include
from .import views

urlpatterns = [
    #URL to call the API showing the details of car manufacturers
    path('api/carmanufacturers', views.viewCarManufacturers, name='viewcarmanufacturers'),

    #URL to call the API showing the model lines/series produced by a car manufacturer
    path('api/carmanufacturers/<int:pk>/series', views.viewCarSeries, name='viewcarseries'),

    #URL to call the API showing the details of parts categories
    path('api/partscategories', views.viewPartsCategories, name='viewpartscategories'),

    #URL to call the API showing the all the items coming under each category irrespective of specific series(s) of a car manufacturer
    path('api/partscategories/<int:pk>/viewallitems', views.viewAllItems, name='viewallitems'),
]