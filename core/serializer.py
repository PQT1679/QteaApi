from rest_framework import serializers
from .models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=("__all__")


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields="__all__"

class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=Orderdetails
        fields="__all__"
        