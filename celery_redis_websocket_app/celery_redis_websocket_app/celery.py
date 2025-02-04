import os

from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_redis_websocket_app.settings')

app = Celery('celery_redis_websocket_app')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')
#
# Load task modules from all registered Django apps.
app.autodiscover_tasks()

# Schedule the ping_hosts task to run every 30 seconds.
app.conf.beat_schedule = {
    'ping-every-30-seconds': {
        'task': 'ping.tasks.ping_hosts',
        'schedule': 30.0,
    },
}