# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import teachers , students , StudentPost

admin.site.register(teachers)
admin.site.register(students)
admin.site.register(StudentPost)