from django.urls import path

from . import views


app_name = "articles"

urlpatterns = [
    path('articles/', views.ArticleView.as_view(), name='ArticleView'),
]