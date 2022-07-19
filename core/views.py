from django.contrib.auth.models import User
# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import *
from rest_framework.decorators import action
from .models import Order, Orderdetails, Product
from rest_framework.response import Response
from .serializer import *
# Create your views here.


class ProductViewSet(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

    permission_classes=[IsAuthenticatedOrReadOnly]
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @action(detail=False,methods=['post'],permission_classes=[IsAdminUser])
    def add_product(self,request,pk=None):
        return Response({'status':self.get_object()})

    @action(detail=False,methods=['post'],permission_classes=[AllowAny])
    def update_product(self,request,pk=None):
        return Response({'status':'success'})
    

class OrderViewSet(viewsets.ModelViewSet):
    queryset=Order.objects.all()
    serializer_class=OrderSerializer


    permission_classes=[IsAuthenticated]
    def create(self, request, *args, **kwargs):
        self.check_permissions
        print(request.data)
        result= super().create(request, *args, **kwargs).data
        result['details']='ahoooo'
        print(result)
        return Response({"status":"nope"})
        return super().create(request, *args, **kwargs)


    permission_classes=[AllowAny]
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    permission_classes=[IsAuthenticated]
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


    permission_classes=[AllowAny]
    def retrieve(self, request, *args, **kwargs):
        result=super().retrieve(request, *args, **kwargs)
        details=Orderdetails.objects.filter(orderid=result.data['orderid'])
        serializer=OrderDetailSerializer(details,many=True)
        result.data['details']=serializer.data
        return result

class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
