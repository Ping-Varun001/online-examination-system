

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0006_auto_20260218_1621'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='profile_pic',
        ),
    ]
