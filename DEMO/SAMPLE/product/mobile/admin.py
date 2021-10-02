from django.contrib import admin
from .models import Product
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'dataEntryBy','created','publish','status')
    list_filter = ('status', 'created', 'publish', 'dataEntryBy')
    search_fields = ('name', 'desc')
    prepopulated_fields = {'slug': ('name',)}
    raw_id_fields = ('dataEntryBy',)
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']
admin.site.register(Product, ProductAdmin)
