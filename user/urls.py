from django.urls import path
from .views import *
urlpatterns = [
    path('', UserLViewSpecial.as_view()),
    path('<int:pk>', UserRViewSpecial.as_view())
]
