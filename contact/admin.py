from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Contact



@admin.register(Contact)
class ContactAdmin(SummernoteModelAdmin):
    list_display = ('opening', )
    summernote_fields = ('body',)


# Register your models here.
