from rest_framework.routers import DefaultRouter
from .views_viewset import TeachersViewSet, StudentsViewSet

router = DefaultRouter()
router.register(r'teachers', TeachersViewSet)
router.register(r'students', StudentsViewSet)

urlpatterns = router.urls