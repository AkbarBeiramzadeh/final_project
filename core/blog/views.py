from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.views import View

from blog.forms import CommentCreateForm, CommentReplyForm
from blog.models import Post


class HomeView(ListView):
    model = Post
    context_object_name = 'posts'


class PostDetailView(View):
    form_class = CommentCreateForm
    form_class_reply = CommentReplyForm

    def setup(self, request, *args, **kwargs):
        self.post_instance = get_object_or_404(Post, pk=kwargs['pk'])
        return super().setup(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        comments = self.post_instance.pcomments.filter(is_reply=False)
        return render(request, 'blog/post_detail.html',
                      {'post': self.post_instance, 'comments': comments, 'form': self.form_class,
                       'reply_form': self.form_class_reply})
