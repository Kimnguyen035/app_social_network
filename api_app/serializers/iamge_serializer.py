from rest_framework import serializers
from ..models.image import Img
from .action_seralizer import ActionSerializer
from configs.variable_response import *


class ImgSerializer(serializers.ModelSerializer, ActionSerializer):
    
    # ============================= function contructor =======================
    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)
        not_fields = kwargs.pop('not_fields', None)
        super().__init__(*args, **kwargs)
        list_key = list(self.get_fields().keys())
        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)
        if not_fields is not None:
            for item in not_fields:
                self.fields.pop(item)
    # ============================== end contructor ===========================
    
    class Meta:
        model = Img
        fields = ['id','image','src_image','status_id','created_at','updated_at','deleted_at']