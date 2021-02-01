from django.http import HttpResponse
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
from user.models import UserModel, FriendRequest
from user.serializers import UserSerializer, FriendRequestSerializer


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
        serializer.save(user=self.request.user)
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
        serializer.save(user=self.request.user)
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


class FriendRequestLCView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    serializer_class = FriendRequestSerializer
    queryset = FriendRequest.objects.all()

    def post(self, request, userId):
        from_user = request.user
        to_user = UserModel.objects.get(id=userId)
        friend_request, created = FriendRequest.objects.get_or_create(from_user=from_user, to_user=to_user)
        if created:
            return HttpResponse("Friend request send")
        else:
            return HttpResponse("Friend request has been already send")


class FriendRequestRUDView(APIView):
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
            return HttpResponse("Friend request accepted")
        else:
            return HttpResponse("Friend request denied")
