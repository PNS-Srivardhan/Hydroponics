from django.shortcuts import render
import json
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from .models import CropFixedValues, CultivatingCrop
from .serializers import CropFixedValuesSerializer, CultivatingCropSerializer
from django.shortcuts import get_object_or_404

ESP8266_URL = "http://192.168.137.7/update"  # ✅ ESP8266 API Endpoint


def index(request):
    return render(request, 'index.html')


class CropFixedValuesViewSet(viewsets.ModelViewSet):
    queryset = CropFixedValues.objects.all()
    serializer_class = CropFixedValuesSerializer

class CultivatingCropViewSet(viewsets.ModelViewSet):
    queryset = CultivatingCrop.objects.all()
    serializer_class = CultivatingCropSerializer

def crop_list(request):
    crops = CropFixedValues.objects.all()  # ✅ Fetch crops
    return render(request, 'index.html', {'crops': crops})

@csrf_exempt
@csrf_exempt  # Disable CSRF for this API endpoint
def send_to_esp8266(request, id):
    if request.method == "POST":
        try:
            # Parse JSON from request body
            body = json.loads(request.body)
            esp_ip = body.get("esp_ip")  # Get ESP8266 IP from frontend

            if not esp_ip:
                return JsonResponse({"success": False, "message": "ESP8266 IP address is required!"})

            # Fetch crop details
            crop = get_object_or_404(CropFixedValues, id=id)
            
            data = {
                "crop_id": crop.id,
                "crop_name": crop.crop_name,
                "min_tds": crop.min_tds,
                "max_tds": crop.max_tds,
                "min_ph": crop.min_ph,
                "max_ph": crop.max_ph,
                "min_humidity": crop.min_humidity,
                "max_humidity": crop.max_humidity,
                "min_water_temp": crop.min_water_temp,
                "max_water_temp": crop.max_water_temp,
                "min_atmosphere_temp": crop.min_atmosphere_temp,
                "max_atmosphere_temp": crop.max_atmosphere_temp,
                "growth_days": crop.growth_days
            }

            # Use the IP provided by the frontend
            ESP8266_URL = f"http://{esp_ip}/update"
            response = requests.post(ESP8266_URL, json=data, timeout=5)

            if response.status_code == 200:
                return JsonResponse({"success": True, "message": "Data sent successfully!"})
            else:
                return JsonResponse({"success": False, "message": f"ESP8266 responded with status {response.status_code}."})

        except json.JSONDecodeError:
            return JsonResponse({"success": False, "message": "Invalid JSON data!"})
        except requests.exceptions.RequestException as e:
            return JsonResponse({"success": False, "message": f"Failed to connect to ESP8266: {str(e)}"})

    return JsonResponse({"success": False, "message": "Invalid request method!"})


def sensor_data(request):
    if request.method == 'POST':
        try:
            # Parse the incoming JSON data
            data = json.loads(request.body)

            # Extract sensor values from the JSON data
            tds = data.get('TDS')
            ph = data.get('pH')
            humidity = data.get('Humidity')
            water_temp = data.get('WaterTemp')
            air_temp = data.get('AirTemp')

            # Save the data to the database
            sensor_data = SensorData.objects.create(
                tds=tds,
                ph=ph,
                humidity=humidity,
                water_temp=water_temp,
                air_temp=air_temp
            )

            # Return a success response
            return JsonResponse({"message": "Sensor data received successfully!"}, status=200)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    # Handle invalid request method
    return JsonResponse({"error": "Invalid request method. Only POST is allowed."}, status=400)

