from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from events.models import Event, Registration
from events.serializers import EventSerializer, UserSerializer


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an event to edit it.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user


class UserRegister(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# GET /api/events/create/
class EventCreate(generics.CreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# GET /api/events/owned/ - List Events Created by the Logged-in User
class OwnedEventListView(generics.ListAPIView):
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        This view should return a list of all events
        for the currently authenticated user.
        """
        return Event.objects.filter(owner=self.request.user)


# GET /api/events/ - List All Events
class EventListView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.AllowAny]  # Assuming events can be listed by any user


# PUT /api/events/<id>/ - Edit an Event (Restricted to the Event's Owner)
class EventDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]


# POST /api/events/<id>/register/ - Register for an Event
class RegisterEventView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        event_id = kwargs.get('pk')
        event = generics.get_object_or_404(Event, id=event_id)
        user = request.user

        if event.registrations.count() >= event.max_attendees:
            return Response({'message': 'This event has reached its maximum number of participants.'},
                            status=status.HTTP_400_BAD_REQUEST)

        # Check if the User is already registered
        if Registration.objects.filter(event=event, user=user).exists():
            return Response({'message': 'You are already registered for this event.'},
                            status=status.HTTP_400_BAD_REQUEST)

        # Register the User
        Registration.objects.create(event=event, user=user)
        return Response({'message': 'Registration successful.'}, status=status.HTTP_201_CREATED)


# POST /api/events/<id>/unregister/ - Unregister for an Event
class UnregisterEventView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        event_id = kwargs.get('pk')
        event = generics.get_object_or_404(Event, id=event_id)
        user = request.user

        # Attempt to unregister the user
        try:
            registration = Registration.objects.get(event=event, user=user)
            registration.delete()
            return Response({'message': 'Unregistered successfully.'}, status=status.HTTP_202_ACCEPTED)
        except Registration.DoesNotExist:
            return Response({'message': 'You are not registered for this event'}, status=status.HTTP_400_BAD_REQUEST)
