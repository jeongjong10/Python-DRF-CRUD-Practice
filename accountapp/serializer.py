from rest_framework import serializers # serializer 임포트
from accountapp.models import User # 모델 임포트

# serializer 란?

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User # 모델 선택
        fields = ('id','username', 'userage', 'marriage')
        # id 필드 : autoincrement 자동 적용


