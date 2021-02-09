from rest_framework.serializers import ModelSerializer

from .models import UserModel, FriendRequest, MessengerModel


class UserSerializer(ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        return UserModel.objects.create_user(**validated_data)


class FriendRequestSerializer(ModelSerializer):
    class Meta:
        model = FriendRequest
        fields = '__all__'


class MessengerSerializer(ModelSerializer):
    class Meta:
        model = MessengerModel
        fields = '__all__'
        extra_kwargs = {'sender': {'read_only': True},
                        'sender_name': {'read_only': True}}
