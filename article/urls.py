from django.urls import path
from . import views


urlpatterns = [
     # URL pattern for the article list page - which is home page
     path('', views.ArticleList.as_view(), name='home'),
     # URL pattern for viewing a single article - identified by its slug
     path('<slug:slug>/', views.single_article, name='single_article'),
     # URL pattern for editing a comment by its ID on single article page
     path('<slug:slug>/edit_comment/<int:comment_id>',
          views.article_comment_edit, name='article_comment_edit'),
     # URL pattern for deleting a comment by its ID on single article page
     path('<slug:slug>/delete_comment/<int:comment_id>',
          views.article_comment_delete, name='article_comment_delete'),
]
