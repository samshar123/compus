# Generated by Django 4.1.9 on 2023-11-05 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_remove_subservice_parent_service_subs'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='subservice',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
