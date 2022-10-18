from __future__ import absolute_import, unicode_literals
import time
from celery import shared_task
from .models import EmailTemplate


@shared_task()
def send_mail(key, menssagem, email, contador):
    time.sleep(contador * 60)
    EmailTemplate.send(
        key, {
            "mensagem": menssagem,
        }
        , emails=[email],
    )
    return True

