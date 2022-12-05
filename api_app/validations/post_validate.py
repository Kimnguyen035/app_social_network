from rest_framework import serializers
from ..models.post import Post
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