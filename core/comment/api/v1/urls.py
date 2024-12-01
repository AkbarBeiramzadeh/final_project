from . import views
from rest_framework.routers import SimpleRouter

app_name = "api-v1"
router = SimpleRouter()
router.register("comment", views.CommentList, basename="comment")
urlpatterns = router.urls
