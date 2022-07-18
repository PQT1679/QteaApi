from venv import create
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import *
from rest_framework.decorators import action
from .models import Order, Orderdetails, Product
from rest_framework.response import Response
from .serializer import OrderDetailSerializer, OrderSerializer, ProductSerializer
# Create your views here.


class ProductViewSet(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

    @action(detail=False,methods=['post'],permission_classes=[IsAdminUser])
    def add_product(self,request,pk=None):
        return Response({'status':self.get_object()})

    @action(detail=False,methods=['post'],permission_classes=[AllowAny])
    def update_product(self,request,pk=None):
        return Response({'status':'success'})
    

class OrderViewSet(viewsets.ModelViewSet):
    queryset=Order.objects.all()
    serializer_class=OrderSerializer

    def create(self, request, *args, **kwargs):
        print(request.data)
        result= super().create(request, *args, **kwargs).data
        result['details']='ahoooo'
        print(result)
        return Response({"status":"nope"})
        return super().create(request, *args, **kwargs)


    permission_classes=[AllowAny]
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


    permission_classes=[AllowAny]
    def retrieve(self, request, *args, **kwargs):
        result=super().retrieve(request, *args, **kwargs)
        details=Orderdetails.objects.filter(orderid=result.data['orderid'])
        serializer=OrderDetailSerializer(details,many=True)
        result.data['details']=serializer.data
        return result