# Generated by Django 4.1.4 on 2023-01-02 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Toggles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(max_length=40)),
                ('info_toggle', models.BooleanField(default=False)),
                ('processguides_toggle', models.BooleanField(default=False)),
                ('scholarships_toggle', models.BooleanField(default=False)),
                ('courses_toggle', models.BooleanField(default=False)),
                ('markers_toggle', models.BooleanField(default=False)),
                ('chatbot_toggle', models.BooleanField(default=False)),
                ('web_analytics_toggle', models.BooleanField(default=False)),
            ],
        ),
    ]
