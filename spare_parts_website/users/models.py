from django.db import models
from django.contrib.auth.models import User
from products.models import Items

#Addresses of an user
class UserAddresses(models.Model):
    ad_id = models.IntegerField(primary_key=True)
    ad_country = models.CharField(null=False, max_length=50)
    ad_state = models.CharField(null=False, max_length=50)
    ad_city = models.CharField(null=False, max_length=50)
    ad_full_address = models.CharField(null=False, max_length=100)
    ad_pin = models.IntegerField(null=False)
    ad_ph_number = models.IntegerField(null=False)
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)


#Cart of a user
class UserCarts(models.Model):
    uc_id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    item = models.ForeignKey(Items, null=False, on_delete=models.CASCADE)

#Products/Items ordered by users
class OrderedItems(models.Model):
    o_id = models.IntegerField(primary_key=True)
    item = models.ForeignKey(Items, null=False, on_delete=models.CASCADE)
    o_quantity = models.IntegerField(null=False)
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    address = models.ForeignKey(UserAddresses, null=False, on_delete=models.CASCADE)