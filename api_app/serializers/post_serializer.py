from rest_framework import serializers
from ..models.post import Post
# from ..models.user import User
from .action_seralizer import ActionSerializer
from configs.variable_response import *
from .iamge_serializer import *

class PostSerializer(serializers.ModelSerializer, ActionSerializer):
    user_id = serializers.IntegerField(allow_null = True)
    group_id = serializers.IntegerField(allow_null=True, required=False)
    image_post = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='src_image'
    )
    # image_post = ImgSerializer(many=True,read_only=True)
    # image_post = serializers.StringRelatedField(many=True)
    
    # ============================= function contructor =======================
    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)
        not_fields = kwargs.pop('not_fields', None)
        super().__init__(*args, **kwargs)
        list_key = list(self.get_fields().keys())
        if fields is not None:
            # if not set(fields).issubset(list_key):
            #     raise serializers.ValidationError('fails')
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)
        if not_fields is not None:
            # if not set(not_fields).issubset(list_key):
            #     raise serializers.ValidationError('fails')
            for item in not_fields:
                self.fields.pop(item)
    # ============================== end contructor ===========================
    
    # def validate_user_id(self, value):
    #     queryset = User.objects.filter(id=value)
    #     if not queryset.exists():
    #         raise serializers.ValidationError(ERROR['not_exists'])
    #     return value
    
    class Meta:
        model = Post
        fields = ['id','user_id','group_id','title','content','image_post','created_at','updated_at','deleted_at']