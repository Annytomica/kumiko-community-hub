from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Contact, ContactMessage


# registers Contact in Django admin
# registers summernote settings for Contact in admin
@admin.register(Contact)
class ContactAdmin(SummernoteModelAdmin):
    list_display = ('opening', )
    summernote_fields = ()


# registers ContactMessage in Django admin
# registers summernote settings for ContactMessage in admin
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_on', 'read',)
