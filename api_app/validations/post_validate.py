from rest_framework import serializers
from ..models.post import Post
from ..models.user import User
from configs.variable_response import *
from ..serializers.post_serializer import *

class IdGetPostValidate(serializers.Serializer):
    id = serializers.IntegerField()
    
    data = PostSerializer(required=False, allow_null=False)
    
    def validate(self, value):
        queryset = Post.objects.filter(id=value['id'])
        if not queryset.exists():
            raise serializers.ValidationError(ERROR['not_exists'])
        value['data'] = queryset.values()[0]
        return value
    
class PostValueValidate(serializers.Serializer):
    user_id = serializers.IntegerField()
    title = serializers.CharField()
    content = serializers.CharField()
    
    def validate_user_id(self, value):
        queryset = User.objects.filter(id=value)
        if not queryset.exists():
            raise serializers.ValidationError(ERROR['not_exists'])
        return value