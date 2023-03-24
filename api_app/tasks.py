from celery import shared_task
from social_network.celery import celery_app
from configs.variable_system import CELERY_QUEUE
from .serializers.post_serializer import *
from configs.variable_response import *
from helpers.response import *

from celery.result import AsyncResult
from datetime import datetime, timedelta

# @shared_task(
    # name='add',
    # bind=True,
    # acks_late=True,
    # autoretry_for=(Exception,),
    # max_retries=3,
    # retry_backoff=True,
    # retry_backoff_max=500,
    # retry_jitter=True,
    # retry_kwargs={'max_retries': 7, 'countdown': 5}
# )

@shared_task(
    autoretry_for=(Exception,),
    retry_kwargs=CELERY_QUEUE['retry_task']
)
def create_blog(value):
    post_save = PostSerializer(data=value)
    if not post_save.is_valid():
        return post_save.errors
    post_save.save()
    return 'success'

@shared_task(
    autoretry_for=(Exception,),
    retry_kwargs=CELERY_QUEUE['retry_task']
)
def add(a, b):
    x = a + b
    return 'x = ' + str(x)