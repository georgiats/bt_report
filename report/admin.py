# -*- coding: utf-8 -*-

import os, sys
from django.contrib import admin
from report.models import *

class ReportAdmin(admin.ModelAdmin):
    fields = ['iTravel_id','bluetooth_logger','system_time','wan_status','sdcard_status']
    list_filter = ['iTravel_id']
    verbose_name='iTravel_id'


