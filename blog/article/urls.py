from django.urls import path

from . import views


app_name = "articles"

urlpatterns = [
    path('articles/', views.ArticleView.as_view(), name='ArticleView'),
    path('articles/<int:pk>/', views.SingleArticleView.as_view(), name='SingleArticle')

]