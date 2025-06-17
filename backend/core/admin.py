from django.contrib import admin
from .models import DisasterEvent

@admin.register(DisasterEvent)
class DisasterEventAdmin(admin.ModelAdmin):
    list_display = ('title', 'disaster_type', 'location', 'timestamp', 'severity')
    search_fields = ('title', 'location', 'disaster_type')