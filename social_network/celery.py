import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'social_network.settings')

celery_app = Celery('social_network')
celery_app.config_from_object('django.conf:settings', namespace='CELERY')
celery_app.autodiscover_tasks()