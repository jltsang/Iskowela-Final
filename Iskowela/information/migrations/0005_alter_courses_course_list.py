# Generated by Django 4.1.4 on 2023-01-02 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0004_rename_scholarship_scholarships_scholarship_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='course_list',
            field=models.JSONField(default=[]),
        ),
    ]
