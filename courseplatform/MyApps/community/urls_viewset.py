from rest_framework.routers import DefaultRouter
from .views_viewset import PostsViewSet, ForumsViewSet

router = DefaultRouter()
router.register(r'community/posts', PostsViewSet)
router.register(r'community/forums', ForumsViewSet)

urlpatterns = router.urls