from django.contrib import admin
from .models import Profile, Category, Post
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('post_content',)


admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Post, PostAdmin)



