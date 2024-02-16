from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from events.views import UserRegister

urlpatterns = [
    path('users/register/', UserRegister.as_view(), name='users-register'),
    path('users/login/', TokenObtainPairView.as_view(), name='token-obtain-pair'),  # for access and refresh
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('users/token/verify/', TokenVerifyView.as_view(), name='token-verify'),
]
