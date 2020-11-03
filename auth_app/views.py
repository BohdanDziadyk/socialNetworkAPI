from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from user.models import UserModel
from user.serializers import UserSerializer


# Create your views here.

class RegisterView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
