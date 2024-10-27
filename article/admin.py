from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Article, ArticleComment, ArticleLike

# registers Article in Django admin
# registers summernote settings for Article in admin
@admin.register(Article)
class ArticleAdmin(SummernoteModelAdmin):

    list_display = ('title', 'tags', 'status')
    search_fields = ['title', 'tags']
    list_filter = ('status', 'created_on', 'tags',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ()

# registers ArticleComment in Django admin
# registers summernote settings for ArticleComment in admin
@admin.register(ArticleComment)
class ArticleCommentAdmin(SummernoteModelAdmin):

    list_display = ('post', 'approved', 'created_on')
    list_filter = ('approved', 'created_on', 'author', 'post', )

# registers ArticleLike in Django admin
# registers summernote settings for ArticleLike in admin
@admin.register(ArticleLike)
class ArticleLikeAdmin(SummernoteModelAdmin):

    list_display = ('post', 'like', 'created_on')
    list_filter = ('like', 'created_on', 'author', 'post', )
