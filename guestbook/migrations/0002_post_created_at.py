# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-13 06:04
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('guestbook', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 2, 13, 6, 4, 0, 645120, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
