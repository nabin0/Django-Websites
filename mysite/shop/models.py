from django.db import models

# Create your models here.


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    prod_name = models.CharField(max_length=60, default="")
    prod_id = models.CharField(max_length=60, default="")
    prod_desc = models.CharField(max_length=1000, default="")
    prod_date = models.DateField()
    category = models.CharField(max_length=50, default="")
    sub_category = models.CharField(max_length=40, default="")
    price = models.IntegerField(default=0)
    images = models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return self.prod_name


class Contact(models.Model):
    name_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, default="")
    email = models.CharField(max_length=30, default="")
    phone = models.CharField(max_length=20, default="")
    desc = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.name


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    orderJson = models.CharField(max_length=5000)
    name = models.CharField(max_length=35)
    amount = models.IntegerField(default=0)
    email = models.CharField(max_length=35)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=35)
    zip = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class UpdateTracker(models.Model):
    order_id = models.CharField(max_length=50)
    update_id = models.AutoField(primary_key=True)
    update_desc = models.CharField(max_length=35)
    timeNow = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.order_id
