from rest_framework.routers import DefaultRouter
from .views_viewset import CoursesViewSet, ModulesViewSet, LessonsViewSet, RegistrationsViewSet

router = DefaultRouter()
router.register(r'courses', CoursesViewSet)
router.register(r'modules', ModulesViewSet)
router.register(r'lessons', LessonsViewSet)
router.register(r'registrations', RegistrationsViewSet)

urlpatterns = router.urls