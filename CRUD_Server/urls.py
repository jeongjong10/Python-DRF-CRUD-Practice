"""
URL configuration for CRUD_Server project.
라우팅하는 파일
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # 레스트 프레임워크 라우팅
    path('api-auth', include('rest_framework.urls')),
    
    # account app으로 라우팅
    path('accounts/', include('accountapp.urls')),
]
