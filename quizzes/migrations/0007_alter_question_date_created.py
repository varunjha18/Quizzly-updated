# Generated by Django 3.2.3 on 2021-05-28 19:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0006_auto_20210529_0041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='date_created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 29, 0, 51, 15, 817307)),
        ),
    ]
