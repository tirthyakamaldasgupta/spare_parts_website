from django.db import models

#Car manufacturers (For example, BMW, Chevrolet)
class CarManufacturers(models.Model):
    cm_id = models.IntegerField(primary_key=True)
    cm_name = models.CharField(null=False, max_length=50)

    def __str__(self):
        return self.cm_name

#Model lines/series produced by car manufacturers (For example, Chevrolet has three model lines namely, AVEO, BEAT, CAPTIVA, under each of which they produce many cars)
class CarSeries(models.Model):
    cs_id = models.IntegerField(primary_key=True)
    cs_name = models.CharField(null=False, max_length=50)
    car_manufacturer = models.ForeignKey(CarManufacturers, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.cs_name

#Categories of parts (For example, Body, Engine etc.)
class PartsCategories(models.Model):
    pc_id = models.IntegerField(primary_key=True)
    pc_name = models.CharField(null=False, max_length=50)

    def __str__(self):
        return self.pc_name

#Products/Items (For example, a body or engine part made for all the models of a series of a car manuacturer)
class Items(models.Model):
    i_id = models.IntegerField(primary_key=True)
    i_name = models.CharField(null=False, max_length=1000)
    parts_category = models.ForeignKey(PartsCategories, null=False, on_delete=models.CASCADE)
    car_series = models.ForeignKey(CarSeries, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.i_name