# Generated by Django 3.0.1 on 2021-06-18 11:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0040_auto_20210618_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='date_created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 6, 18, 16, 48, 21, 695330)),
        ),
    ]
