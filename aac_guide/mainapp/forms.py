from django import forms
from .models import Post
from django_summernote.widgets import SummernoteWidget


class PostForm(forms.ModelForm):


    class Meta:
        model = Post

        fields = ('post_title', 'post_content', 'post_image',)

        widgets = {
            'post_content' : SummernoteWidget(),
        }


        