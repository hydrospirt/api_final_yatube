from django.urls import path, include
from rest_framework import routers

from api.views import PostViewSet, CommentViewSet

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
]
