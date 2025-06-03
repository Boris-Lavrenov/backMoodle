
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter

from myapi.views import UserViewSet

router = DefaultRouter()
router.register('user2', UserViewSet)

urlpatterns = router.urls