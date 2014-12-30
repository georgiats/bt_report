# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('iTravel_id', models.CharField(max_length=200)),
                ('bluetooth_logger', models.CharField(max_length=200)),
                ('system_time', models.CharField(max_length=200)),
                ('wan_status', models.CharField(max_length=200)),
                ('sdcard_status', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
