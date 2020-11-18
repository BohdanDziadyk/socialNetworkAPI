from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from rest_framework_simplejwt.views import TokenRefreshView
from user.models import UserModel
from user.serializers import UserSerializer


# Create your views here.

class RegisterView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()


class InvalidTokenSpecial(InvalidToken):
    status_code = status.HTTP_403_FORBIDDEN


class TokenRefreshViewSpecial(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidTokenSpecial(e.args[0])

        return Response(serializer.validated_data, status=status.HTTP_200_OK)
