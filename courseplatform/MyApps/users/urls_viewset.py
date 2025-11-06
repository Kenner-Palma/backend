from rest_framework.routers import DefaultRouter
from .views_viewset import TeachersViewSet, StudentsViewSet

router = DefaultRouter()
router.register(r'users/teachers', TeachersViewSet)
router.register(r'users/students', StudentsViewSet)

urlpatterns = router.urls