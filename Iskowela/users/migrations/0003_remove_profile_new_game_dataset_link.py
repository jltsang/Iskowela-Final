# Generated by Django 3.0.4 on 2020-04-09 03:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200409_1126'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='new_game_dataset_link',
        ),
    ]