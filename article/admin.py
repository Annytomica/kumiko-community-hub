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


@admin.register(ArticleComment)
class ArticleCommentAdmin(SummernoteModelAdmin):

    list_display = ('post', 'approved', 'created_on')
    list_filter = ('approved', 'created_on', 'author', 'post', )


@admin.register(ArticleLike)
class ArticleLikeAdmin(SummernoteModelAdmin):

    list_display = ('post', 'like', 'created_on')
    list_filter = ('like', 'created_on', 'author', 'post', )
