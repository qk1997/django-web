# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-21 13:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='headimg',
            new_name='headImg',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='username',
        ),
    ]
