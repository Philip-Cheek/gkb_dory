from django.contrib import admin
from .models import *
# Register your models here.

class ItemOptionAdmin(admin.ModelAdmin):
	list_display = ['option', 'price', 'requisites']

admin.site.register(CategoryOption)
admin.site.register(ItemOption, ItemOptionAdmin)



