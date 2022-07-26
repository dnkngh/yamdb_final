from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    CategoryViewSet,
    CommentViewset,
    GenreViewSet,
    ReviewViewset,
    TitleViewSet,
    UsersViewSet,
    signup,
    token
)

app_name = 'api'

router = DefaultRouter()

router.register('categories', CategoryViewSet)
router.register('genres', GenreViewSet)
router.register('titles', TitleViewSet)
router.register('users', UsersViewSet, basename='users')
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewset,
    basename='comments'
)
router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewset,
    basename='reviews'
)

v1_auth_patterns = [
    path('token/', token, name='get_token'),
    path('signup/', signup, name='signup'),
]

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/', include(v1_auth_patterns)),
]
