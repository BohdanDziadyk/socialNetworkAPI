from rest_framework.serializers import ModelSerializer

from .models import UserModel


class UserSerializer(ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('id', 'username', 'email', 'password', 'is_superuser', 'phone')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        return UserModel.objects.create_user(**validated_data)


