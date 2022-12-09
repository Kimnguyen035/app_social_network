from celery import shared_task
from django.core.cache import caches
from configs.variable_system import *
from .serializers.post_serializer import *

# @shared_task(
    # name='add',
    # bind=True,
    # acks_late=True,
    # autoretry_for=(Exception,),
    # max_retries=3,
    # retry_backoff=True,
    # retry_backoff_max=500,
    # retry_jitter=True
# )
@shared_task
def add(value):
    post_save = PostSerializer(data=value)
    if not post_save.is_valid():
        return post_save.errors
    post_save.save()
    return post_save.data