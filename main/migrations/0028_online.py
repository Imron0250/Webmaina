# Generated by Django 4.1.4 on 2022-12-08 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0027_rename_title_result_title1_result_title2_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='online',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.CharField(max_length=255)),
                ('tweeter', models.CharField(max_length=255)),
            ],
        ),
    ]