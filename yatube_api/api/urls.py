from django.urls import path, include
from rest_framework import routers

from api.views import PostViewSet, CommentViewSet, GroupViewSet, FollowViewSet

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comments')
router.register(r'groups', GroupViewSet, basename='groups')
router.register(r'follow', FollowViewSet, basename='follows')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls.jwt'))
]
