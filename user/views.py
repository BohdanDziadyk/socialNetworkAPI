from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response

from .models import UserModel
from .serializers import UserSerializer


class UserLViewSpecial(ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    queryset = UserModel.objects.all()

    def list(self, request, *args, **kwargs):
        qs = self.get_queryset().exclude(id=self.request.user.id)
        return Response(UserSerializer(qs, many=True).data)


class UserRViewSpecial(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()

