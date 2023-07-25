from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

# 기존 장고의 방식 (함수, 클래스 방식)
def hello_world(request):
    return HttpResponse("Hello world")

# DRF 방식 Function based View
@api_view()
def drf_hello_world(request):
    return Response({"message" : "hello world"})

# DRF API 문서 자동 생성

