from django.apps import AppConfig
from django.contrib.auth import get_user_model
import os
from django.db.utils import OperationalError

class ExamConfig(AppConfig):
    name = 'exam'

    def ready(self):
        try:
            User = get_user_model()

            username = os.environ.get('DJANGO_SUPERUSER_USERNAME')
            email = os.environ.get('DJANGO_SUPERUSER_EMAIL')
            password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')

            if not username or not password:
                return  # env vars not set

            if not User.objects.filter(username=username).exists():
                User.objects.create_superuser(
                    username=username,
                    email=email,
                    password=password
                )
                print("✅ Superuser created automatically")

        except OperationalError:
            # DB not ready during migrate
            pass