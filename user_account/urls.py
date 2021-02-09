from django.urls import path
from .views import *

urlpatterns = [
    path('', UserAccountRUDViewSpecial.as_view()),
    path('posts', UserPostsLCView.as_view()),
    path('posts/<int:pk>', UserPostsRUDView.as_view()),
    path('comments', UserCommentsLCView.as_view()),
    path('comments/<int:pk>', UserCommentsRUDView.as_view()),
    path('friends', UserFriendsLView.as_view()),
    path('friends/send_friend_request/<int:userId>', FriendRequestLCView.as_view(), name="send friend request"),
    path('friends/accept_friend_request/<int:requestId>', FriendRequestRUDView.as_view(), name="accept_friend_request"),
    path('messages', MessengerLCView.as_view()),
    # path('messages/received', MessengerLView.as_view())
    path('messages/<int:pk>', MessengerRUDView.as_view())
]
