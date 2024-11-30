from django import forms

from comment.models import Comment
from .models import Post


class PostCreateUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "content", "status", "category", "published_date")


class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        widgets = {
            'body': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Enter your comment here...', 'rows': 3, })
        }


class CommentReplyForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)