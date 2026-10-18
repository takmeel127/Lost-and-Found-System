from django.contrib import admin
from .models import Claim

@admin.register(Claim)
class ClaimAdmin(admin.ModelAdmin):
    list_display = ('user', 'lost_item', 'found_item', 'status', 'created_at')
    list_filter = ('status',)
    search_fields = ('user__email', 'lost_item__name', 'found_item__name')
