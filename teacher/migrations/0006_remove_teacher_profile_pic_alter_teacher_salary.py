

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0005_auto_20260218_1632'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='profile_pic',
        ),
        migrations.AlterField(
            model_name='teacher',
            name='salary',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
