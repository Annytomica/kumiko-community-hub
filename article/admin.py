from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Article, ArticleComment, ArticleLike


@admin.register(Article)
class ArticleAdmin(SummernoteModelAdmin):

    list_display = ('title', 'tags', 'status')
    search_fields = ['title', 'tags']
    list_filter = ('status', 'created_on', 'tags',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ()


# Register your models here.
admin.site.register(ArticleComment)
admin.site.register(ArticleLike)
