from django import forms
from .models import ArticleComment, ArticleLike


class ArticleCommentForm(forms.ModelForm):
    class Meta:
        model = ArticleComment
        fields = ('body',)
        widgets = {
            'body': forms.Textarea(attrs={'placeholder': 'Leave your comment here',})
        }

class ArticleLikeForm(forms.ModelForm):
    class Meta:
        model = ArticleLike
        fields = ('like',)
        widgets = {
            'like': forms.HiddenInput()  # This makes the 'like' field hidden
        }