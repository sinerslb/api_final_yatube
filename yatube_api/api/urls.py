from django.urls import include, path
from rest_framework import routers
from api.views import PostViewSet, GroupViewSet, CommentsViewSet, FollowViewSet

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'groups', GroupViewSet)
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentsViewSet,
    basename='comments'
)
router.register(r'follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('', include('djoser.urls.jwt')),
    path('', include(router.urls)),
]
