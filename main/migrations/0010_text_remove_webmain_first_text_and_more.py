# Generated by Django 4.1.4 on 2022-12-08 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_webmain_first_text_webmain_first_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='text',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('text', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='webmain',
            name='first_text',
        ),
        migrations.RemoveField(
            model_name='webmain',
            name='first_title',
        ),
    ]