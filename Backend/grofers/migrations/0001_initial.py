# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-04-07 02:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=1000)),
                ('value', models.CharField(max_length=1000)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]