from django.shortcuts import render

# Create your views here.
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from post.models import PostModel
from post.serializers import PostSerializer
from user.models import UserModel
from user.serializers import UserSerializer
from comment.models import CommentModel
from comment.serializers import CommentSeriallizer


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


class UserCommentsLCView(ListCreateAPIView):
    serializer_class = CommentSeriallizer
    queryset = CommentModel
    pagination_class = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def list(self, request, *args, **kwargs):
        qs = self.get_queryset().filter(user=self.request.user.id)
        return Response(PostSerializer(qs, many=True).data)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        super().perform_create(serializer)
