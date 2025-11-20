from rest_framework.routers import DefaultRouter
from .views_viewset import PostsViewSet, ForumsViewSet

router = DefaultRouter()
router.register(r'posts', PostsViewSet)
router.register(r'forums', ForumsViewSet)

urlpatterns = router.urls