from django.contrib import admin
from .models import CropData

# Custom admin display for better table view
@admin.register(CropData)
class CropDataAdmin(admin.ModelAdmin):
    list_display = ('year', 'region', 'crop', 'production', 'yield_amount')
    list_filter = ('year', 'region')
    search_fields = ('crop', 'region')