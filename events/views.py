from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from events.models import Event, Registration
from events.serializers import EventSerializer, UserSerializer


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
    permission_classes = [permissions.IsAuthenticated]
