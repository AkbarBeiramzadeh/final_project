from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from blog.forms import CommentCreateForm, CommentReplyForm, PostCreateUpdateForm
from blog.models import Post
from django.contrib import messages

from comment.models import Comment


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

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.user = request.user
            new_comment.post = self.post_instance
            new_comment.save()
            messages.success(request, 'your comment submitted successfully', 'success')
            return redirect('blog:post_detail', self.post_instance.id)


class PostCreateView(View):
    form_class = PostCreateUpdateForm

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, 'blog/post_create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            messages.success(request, 'you created a new post', 'success')
            return redirect('blog:post_detail', new_post.id)


class PostAddReplyView(View):
    form_class = CommentReplyForm

    def post(self, request, post_id, comment_id):
        post = get_object_or_404(Post, id=post_id)
        comment = get_object_or_404(Comment, id=comment_id)
        form = self.form_class(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.user = request.user
            reply.post = post
            reply.reply = comment
            reply.is_reply = True
            reply.save()
            messages.success(request, 'your reply submitted successfully', 'success')
        return redirect('home:post_detail', post.id)


class PostDeleteView(LoginRequiredMixin, View):
    def get(self, request, post_id):
        post = get_object_or_404(Post, pk=post_id)
        if post.author.id == request.user.id:
            post.delete()
            messages.success(request, 'post deleted successfully', 'success')
        else:
            messages.error(request, 'you cant delete this post', 'danger')
        return redirect('blog:home')


class PostUpdateView(LoginRequiredMixin, View):
    form_class = PostCreateUpdateForm

    def setup(self, request, *args, **kwargs):
        self.post_instance = get_object_or_404(Post, pk=kwargs['post_id'])
        return super().setup(request, *args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        post = self.post_instance
        if not post.author.id == request.user.id:
            messages.error(request, 'you cant update this post', 'danger')
            return redirect('blog:home')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        post = self.post_instance
        form = self.form_class(instance=post)
        return render(request, 'blog/post_update.html', {'form': form})

    def post(self, request, *args, **kwargs):
        post = self.post_instance
        form = self.form_class(request.POST, instance=post)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.save()
            messages.success(request, 'you updated this post', 'success')
            return redirect('blog:post_detail', post.id)
