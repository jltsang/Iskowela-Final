# Generated by Django 4.1.7 on 2023-05-12 09:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0010_alter_timetracking_last_update'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetracking',
            name='last_update',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 12, 9, 39, 22, 205490, tzinfo=datetime.timezone.utc)),
        ),
    ]