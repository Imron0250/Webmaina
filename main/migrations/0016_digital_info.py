# Generated by Django 4.1.4 on 2022-12-08 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_faq'),
    ]

    operations = [
        migrations.CreateModel(
            name='Digital_Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adres', models.CharField(max_length=255)),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('desc', models.TextField()),
            ],
        ),
    ]
