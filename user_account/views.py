from django.http import HttpResponse
from django.db.models import Q

# Create your views here.
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from comment.models import CommentModel
from comment.serializers import CommentSeriallizer
from post.models import PostModel
from post.serializers import PostSerializer
from user.models import UserModel, FriendRequest, MessengerModel
from user.serializers import UserSerializer, FriendRequestSerializer, MessengerSerializer


class UserAccountRUDViewSpecial(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def retrieve(self, request, *args, **kwargs):
        qs = self.get_queryset().filter(id=self.request.user.id).first()
        return Response(UserSerializer(qs).data)


class UserPostsLCView(ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = PostModel.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def list(self, request, *args, **kwargs):
        qs = self.get_queryset().filter(user=self.request.user.id)
        return Response(PostSerializer(qs, many=True).data)

    def perform_create(self, serializer):
        user = UserModel.objects.get(id=self.request.user.id)
        serializer.save(user=self.request.user)
        serializer.save(username=user.username)
        super().perform_create(serializer)


class UserPostsRUDView(RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    queryset = PostModel.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]


class UserCommentsLCView(ListCreateAPIView):
    serializer_class = CommentSeriallizer
    queryset = CommentModel.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def list(self, request, *args, **kwargs):
        qs = self.get_queryset().filter(user=self.request.user.id)
        return Response(PostSerializer(qs, many=True).data)

    def perform_create(self, serializer):
        user = UserModel.objects.get(id=self.request.user.id)
        serializer.save(user=self.request.user)
        serializer.save(username=user.username)
        super().perform_create(serializer)


class UserCommentsRUDView(RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSeriallizer
    queryset = CommentModel.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]


class UserFriendsLView(ListAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()

    def list(self, request, *args, **kwargs):
        user = UserModel.objects.get(id=self.request.user.id)
        return Response(UserSerializer(user.friends, many=True).data)


class FriendRequestLView(ListAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    serializer_class = FriendRequestSerializer
    queryset = FriendRequest.objects.all()

    def list(self, request, *args, **kwargs):
        qs = FriendRequest.objects.filter(to_user=self.request.user.id)
        return Response(FriendRequestSerializer(qs, many=True).data)


class FriendRequestCView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    serializer_class = FriendRequestSerializer
    queryset = FriendRequest.objects.all()

    def post(self, request, userId):
        from_user = request.user
        user = UserModel.objects.get(id=self.request.user.id)
        to_user = UserModel.objects.get(id=userId)
        sender_name = user.username
        friend_request, created = FriendRequest.objects.get_or_create(from_user=from_user, to_user=to_user,
                                                                      sender_name=sender_name)
        if created:
            return Response("Friend request send")
        else:
            return Response("Friend request has been already send")


class FriendRequestAcceptView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    serializer_class = FriendRequestSerializer
    queryset = FriendRequest.objects.all()

    def post(self, request, requestId):
        friend_request = FriendRequest.objects.get(id=requestId)
        if friend_request.to_user == request.user:
            friend_request.to_user.friends.add(friend_request.from_user)
            friend_request.from_user.friends.add(friend_request.to_user)
            friend_request.delete()
            return Response("Friend request accepted")
        else:
            return Response("An error has been occurred")


class FriendRequestDeniedView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    serializer_class = FriendRequestSerializer
    queryset = FriendRequest.objects.all()

    def post(self, request, requestId):
        friend_request = FriendRequest.objects.get(id=requestId)
        if friend_request.to_user == request.user:
            friend_request.delete()
            return Response("Friend request denied")
        else:
            return Response("An error has been occurred")


class UserFriendsDeleteView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()

    def post(self, request, userId):
        user = UserModel.objects.get(id=self.request.user.id)
        user.friends.remove(userId)
        friend = UserModel.objects.get(id=userId)
        friend.friends.remove(self.request.user.id)
        return Response("Friend successfully deleted")


class MessengerLCView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    serializer_class = MessengerSerializer
    queryset = MessengerModel.objects.all()

    def list(self, request, *args, **kwargs):
        qs = MessengerModel.objects.filter(Q(sender_id=self.request.user.id) | Q(receiver_id=self.request.user.id))
        return Response(MessengerSerializer(qs, many=True).data)

    def perform_create(self, serializer):
        user = UserModel.objects.get(id=self.request.user.id)
        serializer.save(sender_id=self.request.user.id, sender_name=user.username)
        super().perform_create(serializer)


class MessengerRUDView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    serializer_class = MessengerSerializer
    queryset = MessengerModel.objects.all()
# class MessengerLView(ListAPIView):
#     permission_classes = [IsAuthenticated]
#     authentication_classes = [JWTAuthentication]
#     serializer_class = MessengerSerializer
#     queryset = MessengerModel.objects.all()
#
#     def list(self, request, *args, **kwargs):
#         qs = self.get_queryset().filter(receiver_id=self.request.user.id)
#         return Response(MessengerSerializer(qs, many=True).data)
