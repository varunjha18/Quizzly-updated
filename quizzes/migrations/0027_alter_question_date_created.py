# Generated by Django 3.2.3 on 2021-06-10 17:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0026_alter_question_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='date_created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 6, 10, 22, 46, 27, 21903)),
        ),
    ]