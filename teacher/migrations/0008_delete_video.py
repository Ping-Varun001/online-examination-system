

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0007_video'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Video',
        ),
    ]
