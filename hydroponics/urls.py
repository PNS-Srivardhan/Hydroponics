
from django.contrib import admin
from django.urls import path , include
from crops.views import index 

urlpatterns = [
     path('admin/', admin.site.urls),
    path('', index, name='index'),  # Set index view for homepage
    path('crops/', include('crops.urls')),  # Include your crops app URLs
]