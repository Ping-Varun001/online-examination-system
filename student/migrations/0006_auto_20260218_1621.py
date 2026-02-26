

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_auto_20260209_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='profile_pic',
            field=models.ImageField(blank=True, default='profile_pic/Student/Profile.png', upload_to='profile_pic/Student/'),
        ),
    ]
