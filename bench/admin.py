# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Category,Company,Country,Rating,CurrencyName
# Register your models here.
admin.site.register(Category),
admin.site.register(Company),
admin.site.register(Country),
admin.site.register(Rating),
admin.site.register(CurrencyName),
