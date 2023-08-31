# Generated by Django 2.2.28 on 2023-04-10 04:42

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_grupo', models.PositiveIntegerField(verbose_name='Grupo')),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_level', models.PositiveIntegerField()),
                ('complete', models.BooleanField()),
                ('time', models.DurationField(blank=True, null=True)),
                ('total_mistakes', models.PositiveIntegerField()),
                ('times_played', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_lista', models.PositiveIntegerField()),
                ('nametag', models.CharField(blank=True, max_length=50, null=True)),
                ('id_process', models.CharField(blank=True, max_length=50, null=True)),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Process',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_process', models.CharField(blank=True, max_length=50, null=True)),
                ('levels_data', models.CharField(blank=True, max_length=50, null=True)),
                ('updated_at', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correo_escolar', models.CharField(max_length=50, verbose_name='Correo Escolar')),
                ('username', models.CharField(max_length=50, verbose_name='Usuario')),
                ('password', models.CharField(max_length=50, verbose_name='Contraseña')),
                ('grupo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Grupo')),
            ],
        ),
        migrations.AddField(
            model_name='grupo',
            name='player',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Player'),
        ),
    ]