from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.PostsListView.as_view(), name='posts_list'),
    path('posts/list/<str:tag_slug>',
         views.PostsListView.as_view(), name='posts_by_tag'),
    path('posts/detail/<int:pk>/<str:slug>',
         views.PostsDetailView.as_view(), name='posts_detail'),
    path('comments/create/<int:pk>',
         views.PostsDetailView.as_view(), name='create_comments')
]

app_name = 'blog'
