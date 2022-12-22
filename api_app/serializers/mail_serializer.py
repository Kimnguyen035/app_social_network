from rest_framework import serializers
from ..models.mail import Mail
from .action_seralizer import ActionSerializer
# from configs.variable_response import *


class MailSerializer(serializers.ModelSerializer, ActionSerializer):
    status = serializers.IntegerField(allow_null=True,required=False)
    
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
        model = Mail
        fields = ['id','title','content','from_mail','to','status','description','created_at','updated_at','deleted_at']