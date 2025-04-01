from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CropFixedValuesViewSet, CultivatingCropViewSet, crop_list, send_to_esp8266
from . import views

router = DefaultRouter()
router.register(r'fixed-values', CropFixedValuesViewSet)
router.register(r'cultivating', CultivatingCropViewSet)

urlpatterns = [
    path('api/', include(router.urls)),  
    path('sensor-data/', views.sensor_data, name='sensor_data'),  
    path('', crop_list, name='crop_list'),
    path('send_to_esp8266/<int:id>/', send_to_esp8266, name='send_to_esp8266'),
]

