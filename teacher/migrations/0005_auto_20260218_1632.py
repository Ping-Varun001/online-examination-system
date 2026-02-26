

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0004_auto_20260209_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='profile_pic',
            field=models.ImageField(blank=True, default='profile_pic/Teacher/profile.png', upload_to='profile_pic/Teacher/'),
        ),
    ]
