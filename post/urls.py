from django.urls import path
from .views import *
urlpatterns = [
    path('user_posts/', PostLCViewSpecial.as_view()),
    path('user_posts/<int:pk>', PostRUDViewSpecial.as_view()),
    path('', PostLView.as_view()),
    path('<int:pk>', PostRView.as_view())
]
