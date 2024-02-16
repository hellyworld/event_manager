from rest_framework import serializers
from events.models import Event, Registration
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['username', 'password', 'email']  # TODO we can use email for users login

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'owner', 'name', 'description', 'start_date', 'end_date', 'max_attendees']
        read_only_fields = ['id', 'owner']

    def get_attendees_count(self, obj):
        return obj.registrations.count()


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = ['id', 'event', 'user', 'registration_date']
