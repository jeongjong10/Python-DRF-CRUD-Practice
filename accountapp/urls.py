from django.urls import path, include
from accountapp.views import hello_world, drf_hello_world

# DRF CRUD 라우팅
from rest_framework import routers
from . import views

# 라우터 설정
router = routers.DefaultRouter()
router.register('user', views.UserViewSet)

# acconts/ 패쓰로 라우팅
urlpatterns = [
    path('', include(router.urls)),
    path('hello/', hello_world),
    path('drf_hello/', drf_hello_world)
    
]

