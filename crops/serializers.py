from rest_framework import serializers
from .models import CropFixedValues, CultivatingCrop

class CropFixedValuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CropFixedValues
        fields = '__all__'

class CultivatingCropSerializer(serializers.ModelSerializer):
    class Meta:
        model = CultivatingCrop
        fields = '__all__'
