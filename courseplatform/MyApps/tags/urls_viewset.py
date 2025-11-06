from rest_framework.routers import DefaultRouter
from .views_viewset import TagsViewSet

router = DefaultRouter()
router.register(r'tags', TagsViewSet)

urlpatterns = router.urls