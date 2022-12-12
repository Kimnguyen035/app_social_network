from celery import shared_task
from celery import current_app as task_task
from django.core.cache import caches
from configs.variable_system import *
from .serializers.post_serializer import *
from configs.variable_response import *
from helpers.response import *

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

@shared_task(name='abc')
def create_blog(value):
    post_save = PostSerializer(data=value)
    if not post_save.is_valid():
        return post_save.errors
    post_save.save()
    # return task_task.AsyncResult('task_id')
    return SUCCESS['create_post']