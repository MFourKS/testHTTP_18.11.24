from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BlogViewSet, PostViewSet, TagViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'blogs', BlogViewSet)
router.register(r'posts', PostViewSet)
router.register(r'tags', TagViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('posts/<int:pk>/', PostViewSet.as_view({'get': 'retrieve'}), name='post_detail'),
]
