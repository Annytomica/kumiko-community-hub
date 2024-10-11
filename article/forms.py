from django import forms
from .models import ArticleComment, ArticleLike


class ArticleCommentForm(forms.ModelForm):
    class Meta:
        model = ArticleComment
        fields = ('body',)

class ArticleLikeForm(forms.ModelForm):
    class Meta:
        model = ArticleLike
        fields = ('like',)