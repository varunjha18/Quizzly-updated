# Generated by Django 3.0.1 on 2021-06-18 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='reply_to',
            field=models.IntegerField(blank=True, default=None),
        ),
        migrations.AddField(
            model_name='message',
            name='sender_id',
            field=models.IntegerField(default=0),
        ),
    ]