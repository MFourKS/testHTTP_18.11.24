from rest_framework import serializers
from .models import User, Blog, Post, Tag, Comment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'is_admin']

class BlogSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    authors = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Blog
        fields = ['id', 'title', 'description', 'created_at', 'updated_at', 'owner', 'authors']

class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    blog = serializers.PrimaryKeyRelatedField(queryset=Blog.objects.all())
    tags = serializers.SlugRelatedField(slug_field='name', many=True, queryset=Tag.objects.all())

    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'is_published', 'created_at', 'likes', 'views', 'author', 'blog', 'tags']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())

    class Meta:
        model = Comment
        fields = ['id', 'author', 'post', 'body', 'created_at']
