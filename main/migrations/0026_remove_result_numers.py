# Generated by Django 4.1.4 on 2022-12-08 16:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_result'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='numers',
        ),
    ]