from django.urls import path
from . import views

urlpatterns = [
    path('', views.comment_list, name='comment_list'),
    path('comment_create/', views.comment_create, name='comment_create'),
    path('comment_update/<int:pk>/', views.comment_update, name='comment_update'),
    path('comment_delete/<int:pk>/', views.comment_delete, name='comment_delete'),
]

