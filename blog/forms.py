from django import forms
from .models import Post, Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ["post"]
        labels = {
            "user_name" : "Your Name",
            "user_email" : "Your Email",
            "text" : "Your Comment"
        }


class PostUploadForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'excerpt', 'image', 'slug', 'content', 'author', 'tags']
