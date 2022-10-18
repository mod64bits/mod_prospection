import os
from celery import Celery
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mod_prospection.settings")
app = Celery("mod_prospection")
app.config_from_object("django.conf:settings", namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


# BAsX@JEt3qgTgHW

# A6dlo3erfk0n3u5p7s87dr4jlw2jazrylidxgpe9raafwx4c00h

# redis-18459.c258.us-east-1-4.ec2.cloud.redislabs.com:18459