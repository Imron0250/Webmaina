# Generated by Django 4.1.4 on 2022-12-09 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0031_blog_site_mini_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='webmain',
            name='center',
        ),
        migrations.RemoveField(
            model_name='webmain',
            name='left',
        ),
        migrations.RemoveField(
            model_name='webmain',
            name='rigth',
        ),
    ]
