from rest_framework.routers import DefaultRouter
from .views_viewset import CoursesViewSet, ModulesViewSet, LessonsViewSet, RegistrationsViewSet

router = DefaultRouter()
router.register(r'courses/courses', CoursesViewSet)
router.register(r'courses/modules', ModulesViewSet)
router.register(r'courses/lessons', LessonsViewSet)
router.register(r'courses/registrations', RegistrationsViewSet)

urlpatterns = router.urls