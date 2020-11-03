from rest_framework.serializers import ModelSerializer

from .models import UserModel


class UserSerializer(ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('id', 'username', 'email', 'is_superuser')

    def create(self, validated_data):
        return UserModel.objects.create_user()

