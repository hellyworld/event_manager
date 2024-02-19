from django.contrib.auth.models import User
from drf_spectacular.utils import extend_schema, extend_schema_field
from rest_framework import serializers

from app_events.models import Event, Registration


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        # TODO we can use email for users login
        fields = ['username', 'password', 'email']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class EventSerializer(serializers.ModelSerializer):
    attendees_count = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = ['id', 'owner', 'name', 'description', 'start_date', 'end_date', 'max_attendees', 'attendees_count']
        read_only_fields = ['id', 'owner', 'attendees_count']

    @extend_schema_field(serializers.IntegerField())
    def get_attendees_count(self, obj):
        return obj.registrations.count()


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = ['id', 'event', 'user', 'registration_date']
