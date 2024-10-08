# Generated by Django 4.2.7 on 2023-11-11 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_remove_service_url_remove_subservice_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='director/')),
            ],
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='NumberData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('number', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'NumberData',
                'verbose_name_plural': 'NumberDatas',
                'db_table': '',
            },
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(null=True)),
                ('by_name', models.CharField(max_length=255)),
                ('position', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterModelOptions(
            name='service',
            options={},
        ),
        migrations.RemoveField(
            model_name='service',
            name='subs',
        ),
        migrations.AddField(
            model_name='service',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='service/icons/'),
        ),
        migrations.AlterModelTable(
            name='service',
            table=None,
        ),
    ]
