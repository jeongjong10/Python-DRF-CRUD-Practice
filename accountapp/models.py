from django.db import models

# 모델 정의

class User(models.Model):
    # 프로퍼티 정의
    username = models.CharField(max_length=10)
    userage = models.IntegerField()
    marriage = models.BooleanField()
