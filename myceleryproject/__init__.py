# This will make sure the app is always imported when django start so that shared_task will use this app

from .celery import app as celery_app

_all_ = ('celery_app',)