from asyncore import write
from dataclasses import field
import email
from django.forms import CharField
from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
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

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model=User
        fields=("id","username","password","email","first_name","last_name","is_superuser","is_staff")
        read_only_fields =["is_superuser","is_staff"]
        extra_kwargs = {'password': {'write_only': True}}
    
    def validate_email(self, value):
        if len(User.objects.filter(email=value))>0:
            raise serializers.ValidationError("Email Already Exist!")
        return value
    
    def validate_username(self, value):
        if len(value)<6:
            raise serializers.ValidationError("Username must long than 5 charaters")
        return value
