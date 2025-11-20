from rest_framework.routers import DefaultRouter
from .views_viewset import EvaluationsViewSet, AttemptsViewSet, DeliveriesViewSet, StudentDeliveriesViewSet

router = DefaultRouter()
router.register(r'evaluations', EvaluationsViewSet)
router.register(r'attempts', AttemptsViewSet)
router.register(r'deliveries', DeliveriesViewSet)
router.register(r'studentDeliveries', StudentDeliveriesViewSet)

urlpatterns = router.urls