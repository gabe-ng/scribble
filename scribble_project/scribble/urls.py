from django.urls import path
from . import views

urlpatterns = [
    ################### POST ###############
    path('', views.post_list, name='post_list'),
    path('posts/<int:pk>', views.post_detail, name='post_detail'),
    path('posts/new', views.post_create, name="post_create"),
    path('posts/<int:pk>/edit', views.post_edit, name="post_edit"),
    path('posts/<int:pk>/delete', views.post_delete, name="post_delete"),

    ################### COMMENT ###############
    path('comments/', views.comment_list, name='comment_list'),
    path('comments/<int:id>', views.comment_detail, name='comment_detail'),
    path('comments/new', views.comment_create, name="comment_create"),
    path('comments/<int:id>/edit', views.comment_edit, name="comment_edit"),
    path('comments/<int:id>/delete', views.comment_delete, name="comment_delete"),
]







