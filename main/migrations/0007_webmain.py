# Generated by Django 4.1.4 on 2022-12-08 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_rename_apps_api_android_api_document_api_ios_api_web'),
    ]

    operations = [
        migrations.CreateModel(
            name='Webmain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('text', models.TextField(max_length=255)),
            ],
        ),
    ]
