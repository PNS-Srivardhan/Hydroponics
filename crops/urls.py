from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CropFixedValuesViewSet, CultivatingCropViewSet, crop_list, send_to_esp8266
from .views import sensor_data

router = DefaultRouter()
router.register(r'fixed-values', CropFixedValuesViewSet)
router.register(r'cultivating', CultivatingCropViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', crop_list, name='crop_list'),
    path('send_to_esp8266/<int:id>/', send_to_esp8266, name='send_to_esp8266'),
    path('sensor-data/', sensor_data, name='sensor_data'),  # ✅ Corrected Path
]
