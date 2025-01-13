from django.contrib import admin
from .models import Flat, Complaint


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address', 'owner',)
    readonly_fields = ("created_at",)
    list_display = ('address', 'price', 'new_building', 'construction_year', 'town',)
    list_filter = ('new_building', 'rooms_number', 'has_balcony',)
    list_editable = ('new_building',)
admin.site.register(Flat, FlatAdmin)

class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('user', 'flat_complaint',)
admin.site.register(Complaint, ComplaintAdmin)