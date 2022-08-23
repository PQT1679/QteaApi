from distutils.command.upload import upload
from itertools import product
from django.db import models


class Product(models.Model):
    productid = models.AutoField(db_column='ProductID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=255)
    productimg=models.ImageField(db_column='IMG', max_length=255,upload_to="products/")
    stock = models.IntegerField()

    class Meta:
        db_table = 'product'

class Discount(models.Model):
    discountid = models.AutoField(primary_key=True,db_column='DiscountID')
    productid = models.ForeignKey(Product,models.CASCADE,db_column='productID')  # Field name made lowercase.
    value = models.IntegerField()
    type = models.CharField(max_length=20)
    create_date = models.DateTimeField()
    from_field = models.DateTimeField(db_column='from')  # Field renamed because it was a Python reserved word.
    until = models.DateTimeField()

    class Meta:
        db_table = 'discount'


class Order(models.Model):
    orderid = models.AutoField(db_column='orderID', primary_key=True)  # Field name made lowercase.
    customername = models.CharField(db_column='customerName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    employeeid = models.IntegerField(db_column='employeeID')  # Field name made lowercase.
    time = models.CharField(db_column='Time', max_length=200, blank=True, null=True)  # Field name made lowercase.
    total = models.IntegerField(db_column='Total')  # Field name made lowercase.
    status = models.IntegerField()

    class Meta:
        db_table = 'order'


class Orderdetails(models.Model):
    detailsid = models.AutoField(db_column='detailsID', primary_key=True)  # Field name made lowercase.
    orderid = models.ForeignKey(Order, models.CASCADE, db_column='orderID')  # Field name made lowercase.
    productid = models.ForeignKey(Product, models.CASCADE, db_column='productID')  # Field name made lowercase.
    quantity = models.IntegerField()

    class Meta:
        db_table = 'orderdetails'

class OrderOrderdetails(models.Model):
    order=models.ForeignKey(Order,models.CASCADE)
    details=models.ForeignKey



class Pricing(models.Model):
    pricingid = models.AutoField(db_column='PricingID', primary_key=True)  # Field name made lowercase.
    productid = models.ForeignKey(Product,models.CASCADE,db_column='ProductID')  # Field name made lowercase.
    base_price = models.IntegerField()
    create_date = models.DateTimeField()
    expiry_date = models.DateTimeField()
    in_active = models.CharField(max_length=1)

    class Meta:
        db_table = 'pricing'

    
class Img(models.Model):
    productimg=models.ImageField(db_column='IMG', max_length=255,upload_to="products/")

    class Meta:
        db_table = 'img'