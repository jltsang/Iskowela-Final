# Generated by Django 4.1.7 on 2023-05-12 09:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0008_alter_timetracking_last_update'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetracking',
            name='last_update',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 12, 9, 26, 46, 157847, tzinfo=datetime.timezone.utc)),
        ),
    ]
