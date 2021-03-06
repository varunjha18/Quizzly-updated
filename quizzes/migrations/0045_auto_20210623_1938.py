# Generated by Django 3.0.1 on 2021-06-23 14:08

import datetime
from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0044_auto_20210622_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='correct_answer',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=7),
        ),
        migrations.AlterField(
            model_name='question',
            name='date_created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 6, 23, 19, 38, 17, 114218)),
        ),
    ]
