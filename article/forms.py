from django import forms
from .models import ArticleComment, ArticleLike


class ArticleCommentForm(forms.ModelForm):
    """
    A form for submitting comments on an article.
    
    **Model**
    Uses :model:`article.ArticleComment` to create and update comments.

    **Fields**
    ``body``
        A TextField where users can enter their comment text.

    **Widgets**
    `body`: Configured as a `Textarea` widget with a placeholder text "Leave your comment here". 
    This provides a user-friendly text area for comment input.
    
    **Usage**
    This form is used in the article detail view (`single_article`)
    It allows users to submit comments on a specific article.
    """
    class Meta:
        model = ArticleComment
        fields = ('body',)
        widgets = {
            'body': forms.Textarea(attrs={'placeholder':
                                          'Leave your comment here', })
        }


class ArticleLikeForm(forms.ModelForm):
    """
    A form for liking or unliking an article.
    
    **Model**
    Uses :model:`article.ArticleLike` to create and update the like status.

    **Fields**
    ``like``
        A BooleanField that represents whether the user likes the article or not.

    **Widgets**
    `like`: Configured as a `HiddenInput` widget, meaning this field will not be visible to users.
    This allows toggling of the like status via button without needing direct form input from the user.
    
    **Usage**
    This form is used in the article detail view (`single_article`) to handle the like button
    It allows users to like or unlike an article.
    """
    class Meta:
        model = ArticleLike
        fields = ('like',)
        widgets = {
            'like': forms.HiddenInput()  # This makes the 'like' field hidden
        }
