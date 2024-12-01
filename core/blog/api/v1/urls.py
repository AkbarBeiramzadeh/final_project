from . import views
from rest_framework.routers import SimpleRouter
from django.urls import path

app_name = "api-v1"

# router = DefaultRouter()
# router.register('post', views.PostModelViewSet, basename='post')
# router.register('category', views.CategoryModelViewSet, basename='category')

router = SimpleRouter()
router.register("post", views.PostModelViewSet, basename="post")
router.register("category", views.CategoryModelViewSet, basename="category")

urlpatterns = router.urls

urlpatterns += [
    path('weather/<str:lat>/<str:long>/<str:api_key>/', views.WeatherApi.as_view(), name='weather'),
]
# urlpatterns = [
#     # path('post/', views.post_list, name='post-list'),
#     # path('post/<int:pk>/', views.post_detail, name='post-detail'),
#     # path('post/', views.PostList.as_view(), name='post-list'),
#     # path('post/<int:pk>/', views.PostDetail.as_view(), name='post-detail'),
#     path('post/', views.PostViewSet.as_view({'get': 'list', 'post': 'create'}), name='post-list'),
#     path('post/<int:pk>/', views.PostViewSet.as_view(
#         {'get': 'retrieve', 'put': 'update', 'delete': 'destroy', 'patch': 'partial_update'}),
#          name='post-detail')
# ]
