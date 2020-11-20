from django.urls import path
from .views import *

urlpatterns = [
    path('', UserAccountRUDViewSpecial.as_view()),
    path('posts', UserPostsLCView.as_view())
]
