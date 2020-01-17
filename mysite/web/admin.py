from django.contrib import admin
from .models import Photo, Post



class PostAdmin(admin.ModelAdmin):
    change_list_template = 'web/new.html'\


    class Meta:
        model = Post


admin.site.register(Post, PostAdmin)


class PhotoAdmin(admin.ModelAdmin):
    list_display = ['title', 'timestamp']

    class Meta:
        model = Photo

admin.site.register(Photo, PhotoAdmin)
