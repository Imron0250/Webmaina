# Generated by Django 4.1.4 on 2022-12-08 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0028_online'),
    ]

    operations = [
        migrations.AddField(
            model_name='online',
            name='img_facebook',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='online',
            name='img_tweeter',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
