from . import views
from django.urls import path


urlpatterns = [
    # temporary name = 'home', change back to articles once real homepage created
    path('', views.ArticleList.as_view(), name='home'),
    path('<slug:slug>/', views.single_article, name='single_article'),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.article_comment_edit, name='article_comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
         views.article_comment_delete, name='article_comment_delete'),
]
