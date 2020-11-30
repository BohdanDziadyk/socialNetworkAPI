from rest_framework.serializers import ModelSerializer

from .models import CommentModel


class CommentSeriallizer(ModelSerializer):
    class Meta:
        model = CommentModel
        fields = '__all__'
        extra_kwargs = {'user': {'read_only': True}}