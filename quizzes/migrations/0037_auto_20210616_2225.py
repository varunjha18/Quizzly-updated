# Generated by Django 3.0.1 on 2021-06-16 16:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0036_auto_20210616_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='date_created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 6, 16, 22, 25, 15, 579712)),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='cover_img',
            field=models.ImageField(blank=True, default='../media/aaaaaaa.jpeg', upload_to='photos/%y/%m/'),
        ),
    ]
