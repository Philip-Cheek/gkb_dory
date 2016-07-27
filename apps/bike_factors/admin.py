from django.contrib import admin
from .models import *

# Register your models here.


class BikeOptionAdmin(admin.ModelAdmin):
	list_display = ['option', 'price_factor']

class FeaturesOptionAdmin(admin.ModelAdmin):
	list_display = ['option', 'price_factor']
	

class BrandOptionAdmin(admin.ModelAdmin):
	list_display = ['option', 'price_factor']
	

class CosmeticOptionAdmin(admin.ModelAdmin):
	list_display = ['option', 'price_factor']
	

class FrameOptionAdmin(admin.ModelAdmin):
	list_display = ['option', 'price_factor']
	

admin.site.register(BikeOption, BikeOptionAdmin)
admin.site.register(FeaturesOption, FeaturesOptionAdmin)
admin.site.register(BrandOption, BrandOptionAdmin)
admin.site.register(CosmeticOption, CosmeticOptionAdmin)
admin.site.register(FrameOption, FrameOptionAdmin)