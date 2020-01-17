from django.urls import path
from . import views

app_name = 'webpage'
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:username>/timeline/', views.timeline_view, name='timeline'),
    path('create-post/', views.create_post_view, name='create_post'),
    path('post/<int:post_id>/', views.post_view, name='post'),
    path('post/<int:post_id>/delete/', views.delete_post_view, name='delete_post'),
]
