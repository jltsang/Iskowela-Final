# Generated by Django 4.2.1 on 2023-05-28 13:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0016_alter_timetracking_last_update_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetracking',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 28, 13, 22, 49, 513734, tzinfo=datetime.timezone.utc)),
        ),
    ]
