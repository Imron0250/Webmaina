# Generated by Django 4.1.4 on 2022-12-08 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_remove_result_numers'),
    ]

    operations = [
        migrations.RenameField(
            model_name='result',
            old_name='title',
            new_name='title1',
        ),
        migrations.AddField(
            model_name='result',
            name='title2',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='result',
            name='title3',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='result',
            name='title4',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
