from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import PostModel
from .serializers import PostSerializer


class PostLCViewSpecial(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return PostModel.objects.filter(user=self.request.user)


class PostRUDViewSpecial(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    serializer_class = PostSerializer

    def get_queryset(self):
        return PostModel.objects.filter(user=self.request.user)


class PostLView(ListAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    serializer_class = PostSerializer
    queryset = PostModel.objects.all()

    def get_queryset(self):
        req = self.request
        qs = PostModel.objects.all()
        query = req.query_params.get('user')
        if query:
            return qs.filter(user=query)
        return qs

    def list(self, request, *args, **kwargs):
        qs = self.get_queryset().exclude(user=self.request.user.id)
        return Response(PostSerializer(qs, many=True).data)


class PostRView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    serializer_class = PostSerializer
    queryset = PostModel.objects.all()
