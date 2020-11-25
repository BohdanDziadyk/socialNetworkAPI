from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import CommentModel
from .serializers import CommentSeriallizer


class CommentLCViewSpecial(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    serializer_class = CommentSeriallizer

    def perform_create(self, serializer):
        print(self.request.user.id)
        serializer.save(user=self.request.user.id)
        super().perform_create(serializer)

    def get_queryset(self):
        return CommentModel.objects.filter(user=self.request.user)


class CommentRUDViewSpecial(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    serializer_class = CommentSeriallizer

    def get_queryset(self):
        return CommentModel.objects.filter(user=self.request.user)


class CommentLView(ListAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    serializer_class = CommentSeriallizer
    queryset = CommentModel.objects.all()

    def get_queryset(self):
        req = self.request
        qs = CommentModel.objects.all()
        query_user = req.query_params.get('user')
        query_post = req.query_params.get('post')
        if query_user:
            return qs.filter(user=query_user)
        elif query_post:
            return qs.filter(post=query_post)
        return qs


class CommentRView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    serializer_class = CommentSeriallizer
    queryset = CommentModel.objects.all()
