# Generated by Django 3.0.1 on 2021-06-16 16:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0035_auto_20210616_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='date_created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 6, 16, 22, 23, 30, 231053)),
        ),
    ]
