# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-11-02 09:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ItemInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=100)),
                ('item_type', models.CharField(max_length=100)),
                ('item_desc', models.CharField(max_length=400)),
                ('item_price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'db_table': 'iteminfo',
            },
        ),
    ]
