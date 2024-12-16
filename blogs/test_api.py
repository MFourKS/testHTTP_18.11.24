import pytest
import os
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Blog

os.environ['DJANGO_SETTINGS_MODULE'] = 'blog_service.settings'
@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def test_user(db):
    user = User.objects.create_user(username='testuser', password='password123')
    return user

@pytest.fixture
def test_blog(db, test_user):
    return Blog.objects.create(
        title='Test Blog',
        description='Description of the blog',
        owner=test_user
    )

@pytest.mark.django_db
def test_get_blog(api_client, test_user, test_blog):
    api_client.force_authenticate(user=test_user)
    response = api_client.get(f'/api/blogs/{test_blog.id}/')
    assert response.status_code == status.HTTP_200_OK
    assert response.data['title'] == 'Test Blog'

@pytest.mark.django_db
def test_create_blog(api_client, test_user):
    api_client.force_authenticate(user=test_user)
    payload = {
        'title': 'New Blog',
        'description': 'A new blog for testing',
        'owner': test_user.id
    }
    response = api_client.post('/api/blogs/', payload)
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data['title'] == 'New Blog'

@pytest.mark.django_db
def test_update_blog(api_client, test_user, test_blog):
    api_client.force_authenticate(user=test_user)
    payload = {'title': 'Updated Blog'}
    response = api_client.patch(f'/api/blogs/{test_blog.id}/', payload)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['title'] == 'Updated Blog'

@pytest.mark.django_db
def test_delete_blog(api_client, test_user, test_blog):
    api_client.force_authenticate(user=test_user)
    response = api_client.delete(f'/api/blogs/{test_blog.id}/')
    assert response.status_code == status.HTTP_204_NO_CONTENT
