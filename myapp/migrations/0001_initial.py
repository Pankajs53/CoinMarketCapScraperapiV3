# Generated by Django 5.0.6 on 2024-06-07 17:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CryptoCoin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('crypto_coin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.cryptocoin')),
            ],
        ),
        migrations.CreateModel(
            name='OfficialLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('link', models.URLField()),
                ('crypto_coin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.cryptocoin')),
            ],
        ),
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('url', models.URLField()),
                ('crypto_coin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.cryptocoin')),
            ],
        ),
    ]
