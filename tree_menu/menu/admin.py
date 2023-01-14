from django.contrib import admin

from .models import Menu, Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')
    search_fields = ('name', )
    list_filter = ('name',)

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name', )
    list_filter = ('name',)
