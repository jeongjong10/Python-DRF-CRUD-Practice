from django.urls import path
from accountapp.views import hello_world, drf_hello_world


# acconts/ 패쓰로 라우팅
urlpatterns = [
    path('hello/', hello_world),
    path('drf_hello/', drf_hello_world)
]