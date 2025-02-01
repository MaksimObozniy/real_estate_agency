from django.contrib import admin
from .models import Flat, Complaint, Owner


class OwnerInline(admin.TabularInline):
    model = Owner.property.through
    raw_id_fields = ('owner',)


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address', 'owner',)
    readonly_fields = ("created_at",)

    list_display = ('address',
                    'price',
                    'new_building',
                    'construction_year',
                    'town',)

    list_filter = ('new_building', 'rooms_number', 'has_balcony',)
    list_editable = ('new_building',)
    raw_id_fields = ('liked_by',)
    inlines = [OwnerInline]


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('property',)

@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('user', 'flat',)
