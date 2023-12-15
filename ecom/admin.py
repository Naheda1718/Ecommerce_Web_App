from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('category_name',)}
    list_display=('category_name', 'slug')

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('product_name',)}
    list_display=('product_name', 'slug')

admin.site.register(Products,ProductAdmin)
admin.site.register(Category, CategoryAdmin)
# Register your models here.
