

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0007_auto_20260209_1417'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('video_url', models.URLField()),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
