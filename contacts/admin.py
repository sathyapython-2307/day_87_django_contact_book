from django.contrib import admin
from .models import Contact
from django.core.mail import send_mail
from django.conf import settings

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created_at')
    
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if not change:  # Only send email for new contacts
            subject = f'New Contact Added: {obj.name}'
            message = f'A new contact was added:\n\nName: {obj.name}\nEmail: {obj.email}\nPhone: {obj.phone}'
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [settings.DEFAULT_FROM_EMAIL],  # Send to admin email
                fail_silently=False,
            )
