# Generated by Django 2.2.28 on 2023-04-12 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20230412_0614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='complete_l1',
            field=models.BooleanField(default=False, verbose_name='Complete Level 1'),
        ),
        migrations.AlterField(
            model_name='record',
            name='complete_l2',
            field=models.BooleanField(default=False, verbose_name='Complete Level 2'),
        ),
        migrations.AlterField(
            model_name='record',
            name='complete_l3',
            field=models.BooleanField(default=False, verbose_name='Complete Level 3'),
        ),
    ]