from rest_framework import routers
from .views import MedicamentoViewSet

router = routers.DefaultRouter()
router.register(r'medicamentos', MedicamentoViewSet)

urlpatterns = router.urls
