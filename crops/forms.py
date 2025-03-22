from django import forms
from .models import CropFixedValues

class CropForm(forms.ModelForm):
    class Meta:
        model = CropFixedValues
        fields = ['crop_name', 'min_tds', 'max_tds', 'min_ph', 'max_ph', 
                  'min_humidity', 'max_humidity', 'min_water_temp', 'max_water_temp', 
                  'min_atmosphere_temp', 'max_atmosphere_temp', 'growth_days']
