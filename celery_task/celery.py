from __future__ import absolute_import

from celery import Celery
from celery.schedules import crontab

app = Celery('celery_task')

app.conf.beat_schedule = {
    'every-5-minutes': {
        'task': 'celery_task.tasks.check_connections',
        'schedule': 5 #crontab('*/5'),
    }
}

if __name__ == '__main__':
    app.start()