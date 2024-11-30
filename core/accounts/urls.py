from django.urls import path, include
from . import views

app_name = "accounts"

urlpatterns = [
    path('profile/<int:pk>/', views.ProfileView.as_view(), name='user_profile'),
    path('logout/', views.LogoutUserView.as_view(), name='user_logout'),
    path("register/", views.UserRegisterView.as_view(), name="user_register"),
    path("login/", views.UserLoginView.as_view(), name="user_login"),
    # path('api/v1/', include('accounts.api.v1.urls')),
    # path("api/v2/", include("djoser.urls")),
    # path("api/v2/", include("djoser.urls.jwt")),
]
