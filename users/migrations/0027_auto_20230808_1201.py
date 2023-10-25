# Generated by Django 3.2.13 on 2023-08-08 12:01

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0026_auto_20230228_1526'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_profile_public',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='roles',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('curator', 'Куратор'), ('moderator', 'Модератор'), ('bank', 'Банк'), ('god', 'Бог')], max_length=32), default=list, size=None),
        ),
    ]