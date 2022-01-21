from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, max_length=12)
    class Meta:
        model = CustomUser
        fields = ('email', 'password')

    # def validate(self, attrs):
    #     return super().validate(attrs)

    # def validated_data(self):
    #     return super().validated_data