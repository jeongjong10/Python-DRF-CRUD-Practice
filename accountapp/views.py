from django.shortcuts import render

# 기존 장고의 방식 (함수, 클래스 방식)
from django.http import HttpResponse 

def hello_world(request):
    return HttpResponse("Hello world")

#---------------------------------------------------------

# DRF 방식 Function based View -> DRF API 문서 자동 생성
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view()
def drf_hello_world(request):
    return Response({"message" : "hello world"})

#---------------------------------------------------------

# 데이터 모델과 연결된 엔드포인트를 처리하는 방법
# CRUD API 구성하기
from rest_framework import viewsets     # viewset 임포트
from .models import User                # 모델 임포트
from .serializer import UserSerializer  # serializer 임포트

class UserViewSet(viewsets.ModelViewSet): # ModelViewSet : CRUD 메서드를 지원 
    queryset = User.objects.all()
    serializer_class = UserSerializer





