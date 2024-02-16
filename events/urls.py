from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from events.views import UserRegister, EventListView, EventCreate, OwnedEventListView, EventDetailAPIView, \
    RegisterEventView, UnregisterEventView

urlpatterns = [
    path('users/register/', UserRegister.as_view(), name='users-register'),
    path('users/login/', TokenObtainPairView.as_view(), name='token-obtain-pair'),  # for access and refresh
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('users/token/verify/', TokenVerifyView.as_view(), name='token-verify'),
    path('events/', EventListView.as_view(), name='event-list'),
    path('events/create/', EventCreate.as_view(), name='event-create'),
    path('events/owned/', OwnedEventListView.as_view(), name='owned-events'),
    path('events/<int:pk>/', EventDetailAPIView.as_view(), name='event-detail'),
    path('events/<int:pk>/register/', RegisterEventView.as_view(), name='event-register'),
    path('events/<int:pk>/unregister/', UnregisterEventView.as_view(), name='event-unregister'),
]
