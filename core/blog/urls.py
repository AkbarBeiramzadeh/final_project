from django.urls import path, include
from . import views

app_name = "blog"

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('post/detail/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/create/', views.PostCreateView.as_view(), name='post_create'),
    path('reply/<int:post_id>/<int:comment_id>/', views.PostAddReplyView.as_view(), name='add_reply'),
    path('post/delete/<int:post_id>/', views.PostDeleteView.as_view(), name='post_delete'),
    path('post/update/<int:post_id>/', views.PostUpdateView.as_view(), name='post_update'),
    #
    path("api/v1/", include("blog.api.v1.urls")),
]
