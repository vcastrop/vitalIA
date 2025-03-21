from django.contrib import admin
from .models import Reminder, DocumentReminder

class ReminderAdmin(admin.ModelAdmin):
    list_display = ('appointment_id', 'user_email', 'reminder_time', 'confirmed')  
    list_filter = ('confirmed', 'reminder_time')

class DocumentReminderAdmin(admin.ModelAdmin):
    list_display = ('reminder', 'required_documents')

admin.site.register(Reminder, ReminderAdmin)
admin.site.register(DocumentReminder, DocumentReminderAdmin)
