# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-28 16:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extendeduser',
            name='card',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='payment.UserCard'),
        ),
    ]