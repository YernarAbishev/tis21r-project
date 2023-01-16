from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='homePage'),
    path('about/', views.abouPage, name='aboutPage'),
    path('news/view/', views.newsPage, name='newsPage'),
    path('post/add/', views.addPost, name='addPost'),
    path('post/view/<int:pk>/', views.postDetail, name='postDetail'),
    path('post/delete/<int:pk>/', views.deletePost, name='deletePost'),
    path('post/edit/<int:pk>/', views.editPost, name='editPost'),
]