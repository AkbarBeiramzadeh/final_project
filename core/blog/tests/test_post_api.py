from django.urls import reverse
from rest_framework.test import APIClient
import pytest

from accounts.models import Profile
from accounts.models.users import User
from datetime import datetime


@pytest.fixture
def api_client():
    client = APIClient()
    return client


@pytest.fixture
def common_user():
    user = User.objects.create_user(email="ab@ab.com", password="1020")
    return user


@pytest.fixture
def common_profile():
    user = User.objects.create_user(email="ab@ab.com", password="1020")
    profile = Profile.objects.get(user=user)
    return profile


@pytest.mark.django_db
class TestPostApi:

    def test_get_post_response_200_status(self, api_client, common_user):
        # self.user = User(email="foo@bar.com")  # NB: You could also use a factory for this
        # password = 'some_password'
        # self.user.set_password(password)
        # self.user.save()
        #
        # # Authenticate client with user
        #
        # api_client.login(email=self.user.email, password=password, is_verified=True)
        api_client.force_login(user=common_user)
        url = reverse("blog:api-v1:post-list")
        response = api_client.get(url)
        assert response.status_code == 200

    def test_create_post_response_201_status(self, api_client, common_user):
        url = reverse("blog:api-v1:post-list")
        data = {
            "title": "test",
            "content": "description",
            "status": True,
            "published_date": datetime.now()
        }
        user = common_user
        # api_client.force_login(user=user)
        api_client.force_authenticate(user=user)
        response = api_client.post(url, data)
        assert response.status_code == 201

    def test_create_post_invalid_data_response_400_status(self, api_client, common_user):
        url = reverse("blog:api-v1:post-list")
        data = {
            "title": "test",
            "status": "True",
            "published_date": datetime.now()
        }
        user = common_user
        # api_client.force_login(user=user)
        api_client.force_authenticate(user=user)
        response = api_client.post(url, data)
        assert response.status_code == 400
