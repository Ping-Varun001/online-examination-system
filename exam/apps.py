from django.apps import AppConfig


class examConfig(AppConfig):
    name = 'exam'

from django.apps import AppConfig
from django.contrib.auth import get_user_model
import os

class ExamConfig(AppConfig):
    name = 'exam'

    def ready(self):
        User = get_user_model()
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin',
                email=os.environ.get('EMAIL_HOST_USER'),
                password=os.environ.get('ADMIN_PASSWORD')
            )