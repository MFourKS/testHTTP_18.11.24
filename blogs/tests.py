from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Blog


class BlogAPITestCase(TestCase):
    def setUp(self):

        self.user = User.objects.create_user(username='testuser', password='password123')
        self.client = APIClient()
        self.client.login(username='testuser', password='password123')

#========================================================================================

        self.blog = Blog.objects.create(
            title='Test Blog',
            description='Description of the blog',
            owner=self.user
        )
        self.blog_url = f'/api/blogs/{self.blog.id}/'

    def test_get_blog(self):
        """Тест получения блога по ID"""
        response = self.client.get(self.blog_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Blog')

    def test_create_blog(self):
        """Тест создания нового блога"""
        payload = {
            'title': 'New Blog',
            'description': 'A new blog for testing',
            'owner': self.user.id
        }
        response = self.client.post('/api/blogs/', payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'New Blog')

    def test_update_blog(self):
        """Тест обновления блога"""
        payload = {'title': 'Updated Blog'}
        response = self.client.patch(self.blog_url, payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Updated Blog')

    def test_delete_blog(self):
        """Тест удаления блога"""
        response = self.client.delete(self.blog_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
