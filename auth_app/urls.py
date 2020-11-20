from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from auth_app.views import RegisterView, TokenRefreshViewSpecial

urlpatterns = [
    path('', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshViewSpecial.as_view()),
    path('register/', RegisterView.as_view())
]
