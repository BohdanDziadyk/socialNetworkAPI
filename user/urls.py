from django.urls import path
from .views import *
urlpatterns = [
    path('user_account/', UserLViewSpecial.as_view()),
    path('user_account/edit/', UserRUDViewSecial.as_view()),
    path('', UserLView.as_view()),
    path('<int:pk>', UserRView.as_view())
]
