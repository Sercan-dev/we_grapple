
from django.urls import path
from . import views

app_name = 'web'
urlpatterns = [
    path('', views.home, name='index'),
    path('rules/', views.rules_view, name='rules'),
    path('gallery/', views.gallery_view, name='gallery'),
    path('contact/', views.contact_view, name='contact'),
    path(r'^$', views.home, name="index"),
    path(r'^staff/articles/$', views.all, name="all"),
    path(r'^staff/articles/new/$', views.new, name="new"),
    path(r'^staff/articles/(?P<id>\d+)/$', views.toggle_publish, name="toggle_publish"),

]
