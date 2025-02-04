from django.contrib import admin
from .models import Host, PingResult

@admin.register(Host)
class HostAdmin(admin.ModelAdmin):
    list_display = ('name', 'ip_address', 'mac_address')
    search_fields = ('name', 'ip_address', 'mac_address')
    list_filter = ('ip_address',)

@admin.register(PingResult)
class PingResultAdmin(admin.ModelAdmin):
    list_display = ('host', 'is_alive', 'timestamp')
    list_filter = ('host', 'is_alive')
    ordering = ('-timestamp',)
