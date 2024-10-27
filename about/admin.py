from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import About

# registers About in Django admin
# registers summernote settings for About in admin
@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    list_display = ('opening',)
    summernote_fields = ('body',)
