from django.contrib import admin
from .models import Flat, Complaint, Owner


class OwnerInline(admin.TabularInline):
    model = Owner.owned_flats.through
    raw_id_fields = ('owner',)

class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'owner_pure_phone', 'address', 'owner',)
    readonly_fields = ("created_at",)
    list_display = ('address', 'owner_pure_phone', 'price', 'new_building', 'construction_year', 'town',)
    list_filter = ('new_building', 'rooms_number', 'has_balcony',)
    list_editable = ('new_building',)
    raw_id_fields = ('liked_by',)
    inlines = [OwnerInline]
admin.site.register(Flat, FlatAdmin)

class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('owned_flats',)
admin.site.register(Owner, OwnerAdmin)

class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('user', 'flat_complaint',)
admin.site.register(Complaint, ComplaintAdmin)