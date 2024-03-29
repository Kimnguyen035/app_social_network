import os
from celery import Celery
# from celery.schedules import crontab
# from kombu import Exchange, Queue

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'social_network.settings')

celery_app = Celery('social_network')

celery_app.config_from_object('django.conf:settings', namespace='CELERY')

# log_user_exchange = Exchange('log_user', type='direct')
# celery_app.conf.task_default_queue = 'default'

# celery_app.conf.task_queues = (
#     Queue('log_user', Exchange('log_user'), routing_key='log_user'),
# )
# # celery_app.conf.task_log_user_queue = 'log_user'
# celery_app.conf.task_default_exchange = 'log_user'
# celery_app.conf.task_default_exchange_type = 'direct'
# celery_app.conf.task_default_routing_key = 'log_user'

celery_app.autodiscover_tasks()

# celery_app.conf.beat_schedule = {
#     'Task_one_schedule' : {
#         'task': 'api_app.tasks.add',
#         'schedule': crontab(hour=16, minute=45),
#         # 'kwargs': {},
#         'args': (16, 16)
#     }
# }