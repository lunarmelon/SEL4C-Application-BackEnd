# Generated by Django 2.2.28 on 2023-04-27 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_auto_20230426_1957'),
    ]

    operations = [
        migrations.AddField(
            model_name='score',
            name='mistakes',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='score',
            name='time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]