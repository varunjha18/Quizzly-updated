# Generated by Django 3.2.2 on 2021-05-26 17:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0002_auto_20210526_2327'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='is_public',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='date_created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 26, 23, 29, 57, 495810)),
        ),
    ]