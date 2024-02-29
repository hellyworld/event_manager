from typing import Any, Type

from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import generics, permissions, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from app_events.filters import EventFilter
from app_events.models import Event, Registration
from app_events.serializers import (
    EventSerializer,
    RegistrationSerializer,
    UserSerializer,
)


@extend_schema(request=UserSerializer, responses={201: UserSerializer})
class UserRegister(APIView):
    """
    API View for user registration
    """

    def post(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return_data = UserSerializer(user).data
            return Response(return_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema_view(post=extend_schema(responses={200: EventSerializer}))
class EventCreate(generics.CreateAPIView):
    """
    API View for event creation
    """

    permission_classes = [permissions.IsAuthenticated]
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def perform_create(self, serializer: Type[EventSerializer]):
        serializer.save(owner=self.request.user)


@extend_schema_view(get=extend_schema(responses={200: EventSerializer(many=True)}))
class OwnedEventListView(generics.ListAPIView):
    """
    API View to list all the app_events owned by the authenticated user
    """

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = EventSerializer

    def get_queryset(self) -> list[Event]:
        if getattr(self, "swagger_fake_view", False):
            return Event.objects.none()
        return Event.objects.filter(owner=self.request.user)


@extend_schema_view(get=extend_schema(responses={200: EventSerializer(many=True)}))
class EventListView(generics.ListAPIView):
    """
    API View to list all app_events
    """

    permission_classes = [permissions.AllowAny]
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = EventFilter


@extend_schema_view(
    get=extend_schema(responses={200: EventSerializer}),
    put=extend_schema(responses={200: EventSerializer}),
    patch=extend_schema(responses={200: EventSerializer}),
    delete=extend_schema(responses={204: None}),
)
class EventDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, and deleting an event
    """

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = EventSerializer

    def get_queryset(self):
        user = self.request.user
        return Event.objects.filter(owner=user)


@extend_schema_view(
    post=extend_schema(responses={200: {"message": "Registration successful."}})
)
class RegisterEventView(APIView):
    """
    API View for event registration
    """

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = RegistrationSerializer

    def post(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        event_id = kwargs.get("pk")
        event = generics.get_object_or_404(Event, id=event_id)
        user = request.user

        if event.registrations.count() >= event.max_attendees:
            return Response(
                {
                    "message": "This event has reached its maximum number of participants."
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        if Registration.objects.filter(event=event, user=user).exists():
            return Response(
                {"message": "You are already registered for this event."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        Registration.objects.create(event=event, user=user)
        return Response(
            {"message": "Registration successful."}, status=status.HTTP_201_CREATED
        )


@extend_schema(
    methods=["POST"],
    request=None,
    responses={200: {"message": "Unregistered successfully."}},
)
class UnregisterEventView(APIView):
    """
    API View to unregister from an event
    """

    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request: Request, pk: str) -> Response:
        event = generics.get_object_or_404(Event, id=pk)
        user = request.user

        try:
            registration = Registration.objects.get(event=event, user=user)
            registration.delete()
            return Response(
                {"message": "Unregistered successfully."},
                status=status.HTTP_204_NO_CONTENT,
            )
        except Registration.DoesNotExist:
            return Response(
                {"message": "You are not registered for this event"},
                status=status.HTTP_400_BAD_REQUEST,
            )
