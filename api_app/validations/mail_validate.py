from rest_framework import serializers
from ..models.mail import Mail
from configs.variable_response import *
from ..serializers.mail_serializer import *

class IdGetMailValidate(serializers.Serializer):
    id = serializers.IntegerField()
    
    data = MailSerializer(required=False, allow_null=False)
    
    def validate(self, value):
        queryset = Mail.objects.filter(id=value['id'])
        if not queryset.exists():
            raise serializers.ValidationError(ERROR['not_exists'])
        value['data'] = queryset.values()[0]
        return value