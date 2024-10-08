from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Article, ArticleComment

@admin.register(Article)
class ArticleAdmin(SummernoteModelAdmin):

    list_display = ('title', 'tags', 'status')
    search_fields = ['title', 'tags']
    list_filter = ('status','created_on', 'tags',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


# Register your models here.
admin.site.register(ArticleComment)