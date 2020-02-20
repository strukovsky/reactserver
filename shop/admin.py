# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from shop.models import Product, Order


# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    pass

class OrderAdmin(admin.ModelAdmin):
    pass


admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)