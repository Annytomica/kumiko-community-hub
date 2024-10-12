from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Contact, ContactMessage


# Register your models here.
@admin.register(Contact)
class ContactAdmin(SummernoteModelAdmin):
    list_display = ('opening', )
    summernote_fields = ()



@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_on', 'read',)