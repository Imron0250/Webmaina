# Generated by Django 4.1.4 on 2022-12-08 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_webmain'),
    ]

    operations = [
        migrations.AddField(
            model_name='webmain',
            name='center',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='webmain',
            name='left',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='webmain',
            name='rigth',
            field=models.BooleanField(default=False),
        ),
    ]