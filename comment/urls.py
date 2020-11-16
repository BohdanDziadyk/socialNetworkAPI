from django.urls import path
from .views import *
urlpatterns = [
    path('user_comments/', CommentLCViewSpecial.as_view()),
    path('user_comments/<int:pk>', CommentRUDViewSpecial.as_view()),
    path('', CommentLView.as_view()),
    path('<int:pk>', CommentRView.as_view())
]
