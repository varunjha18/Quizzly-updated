# Generated by Django 3.2.3 on 2021-06-09 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Scores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('quiz_id', models.IntegerField()),
                ('user_name', models.CharField(max_length=200)),
            ],
        ),
    ]
