# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-26 03:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_usergroup'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='email',
            field=models.CharField(default=18611720843, max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userinfo',
            name='test',
            field=models.CharField(max_length=19, null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='user_type_id',
            field=models.IntegerField(choices=[(1, '超级用户'), (2, '普通用户'), (3, '一般用户')], default=1),
        ),
    ]