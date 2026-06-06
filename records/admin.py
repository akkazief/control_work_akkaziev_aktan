from django.contrib import admin

from records.models import Record

class RecordAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'status', 'created_at', 'updated_at')
    list_filter = ('status',)
    search_fields = ('name', 'email', 'text')
    readonly_fields = ('created_at', 'updated_at')
    list_editable = ('status',)

admin.site.register(Record, RecordAdmin)