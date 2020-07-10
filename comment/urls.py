from django.urls import path
from . import views

urlpatterns = [
    path('', views.CommentList.as_view(), name='comment_list'),
    path('comment_create/', views.CommentCreate.as_view(), name='comment_create'),
    path('comment_update/<int:pk>/', views.CommentUpdate.as_view(), name='comment_update'),
    path('comment_delete/<int:pk>/', views.CommentDelete.as_view(), name='comment_delete'),
]

