from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['username', 'password', 'email']  # TODO we can use email for users login

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
