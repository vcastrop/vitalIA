from django.contrib import admin
from .models import Reminder

@admin.register(Reminder)
class ReminderAdmin(admin.ModelAdmin):
    list_display = ('user', 'appointment_date', 'created_at', 'is_active')
    list_filter = ('is_active', 'appointment_date', 'created_at')
    search_fields = ('user__username', 'documents')
    readonly_fields = ('created_at',)
    ordering = ('-appointment_date',)
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('user')
