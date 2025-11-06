from rest_framework.routers import DefaultRouter
from .views_viewset import EvaluationsViewSet, AttemptsViewSet, DeliveriesViewSet, StudentDeliveriesViewSet

router = DefaultRouter()
router.register(r'evaluations/evaluations', EvaluationsViewSet)
router.register(r'evaluations/attempts', AttemptsViewSet)
router.register(r'evaluations/deliveries', DeliveriesViewSet)
router.register(r'evaluations/studentDeliveries', StudentDeliveriesViewSet)

urlpatterns = router.urls