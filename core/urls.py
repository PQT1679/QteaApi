from multiprocessing.managers import BaseManager
from django.contrib import admin
from django.db import router
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import *


router = DefaultRouter()
router.register(r'products',ProductViewSet,basename='products')
router.register(r'orders',OrderViewSet,basename='orders')
router.register(r'users',UserViewSet,basename='user')
router.register(r'imgs',ImageViewset,basename='imgs')
urlpatterns = [
]
urlpatterns+=router.urls
