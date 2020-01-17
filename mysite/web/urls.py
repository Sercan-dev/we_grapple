
from django.urls import path
from . import views

app_name = 'web'
urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('rules/', views.rules_view, name='rules'),
    path('gallery/', views.gallery_view, name='gallery'),
    path(r'^$', views.home, name="index"),
    path(r'^staff/articles/$', views.all, name="all"),
    path(r'^staff/articles/new/$', views.new, name="new"),
    path(r'^staff/articles/(?P<id>\d+)/$', views.toggle_publish, name="toggle_publish"),

]
