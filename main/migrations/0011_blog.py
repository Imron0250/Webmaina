# Generated by Django 4.1.4 on 2022-12-08 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_text_remove_webmain_first_text_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('img', models.ImageField(upload_to='')),
                ('mini_text', models.CharField(max_length=255)),
                ('text', models.TextField()),
            ],
        ),
    ]
