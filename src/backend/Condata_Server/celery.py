import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Condata_Server.settings')

app = Celery('Condata_Server', backend='rpc://', broker='amqp://')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks ()