from django.urls import path
from .views import *

urlpatterns = [
    path('', UserAccountRUDViewSpecial.as_view()),
    path('posts', UserPostsLCView.as_view()),
    path('posts/<int:pk>', UserPostsRUDView.as_view()),
    path('comments', UserCommentsLCView.as_view()),
    path('comments/<int:pk>', UserCommentsRUDView.as_view())
]
