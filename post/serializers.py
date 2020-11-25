from rest_framework.serializers import ModelSerializer

from .models import PostModel


class PostSerializer(ModelSerializer):
    class Meta:
        model = PostModel
        fields = '__all__'
        extra_kwargs = {'user': {'read_only': True}}
