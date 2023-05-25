# Generated by Django 4.1.7 on 2023-03-12 04:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_alter_profile_type'),
        ('analytics', '0002_alter_chatbotmonitor_datetime_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Monitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_visited', models.CharField(blank=True, max_length=50, null=True)),
                ('continent', models.CharField(blank=True, max_length=50, null=True)),
                ('country', models.CharField(blank=True, max_length=50, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('datetime', models.DateTimeField(blank=True, max_length=50, null=True)),
                ('ip', models.CharField(blank=True, max_length=50, null=True)),
                ('profile', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
        ),
    ]