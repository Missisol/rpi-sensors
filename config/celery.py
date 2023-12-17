import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
app = Celery("config")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()


# заносим таски в очередь
app.conf.beat_schedule = {
    'get_bme_data': { 
        'task': 'meteo.tasks.get_bme_data',
        # 'schedule': crontab(), 
        # 'schedule': crontab(minute='*/5'), 
        'schedule': crontab(minute='*/15'), 
    },
    'get_dht_data': { 
        'task': 'meteo.tasks.get_dht_data',
        'schedule': crontab(), 
        # 'schedule': crontab(minute='*/5'), 
        # 'schedule': crontab(minute='*/15'), 
    },
    'get_bme_history': { 
        'task': 'meteo.tasks.get_bme_history',
        # 'schedule': crontab(), 
        # 'schedule': crontab(minute=0, hour='*/1'),
        'schedule': crontab(minute='*/15'), 
    },
    'get_dht_history': { 
        'task': 'meteo.tasks.get_dht_history',
        'schedule': crontab(), 
        # 'schedule': crontab(minute=0, hour='*/1'),
        # 'schedule': crontab(minute='*/15'), 
    },
}

# app.conf.enable_utc = True
app.conf.timezone = 'Europe/Moscow'
