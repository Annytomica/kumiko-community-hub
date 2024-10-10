from . import views
from django.urls import path


urlpatterns = [
    # temporary name = 'home', change back to articles once real homepage created
    path('articles/', views.ArticleList.as_view(), name='home'),
]