from rest_framework.routers import DefaultRouter
from .views import MootCourtViewSet

router = DefaultRouter()
router.register('mootcourts', MootCourtViewSet, 'mootcourt')

urlpatterns = router.urls
