

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0006_remove_teacher_profile_pic_alter_teacher_salary'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=200)),
                ('youtube_link', models.URLField()),
            ],
        ),
    ]
