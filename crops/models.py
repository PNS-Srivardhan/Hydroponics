
# Create your models here.
from django.db import models

class CropFixedValues(models.Model):
    crop_name = models.CharField(max_length=100, unique=True)
    min_tds = models.FloatField()
    max_tds = models.FloatField()
    min_ph = models.FloatField()
    max_ph = models.FloatField()
    min_humidity = models.FloatField()
    max_humidity = models.FloatField()
    min_water_temp = models.FloatField()
    max_water_temp = models.FloatField()
    min_atmosphere_temp = models.FloatField()
    max_atmosphere_temp = models.FloatField()
    growth_days = models.IntegerField()

    def __str__(self):
        return self.crop_name


class CultivatingCrop(models.Model):
    crop = models.ForeignKey(CropFixedValues, on_delete=models.CASCADE)  # Link to fixed values
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(null=True, blank=True)
    current_tds = models.FloatField()
    current_ph = models.FloatField()
    current_humidity = models.FloatField()
    current_water_temp = models.FloatField()
    current_atmosphere_temp = models.FloatField()
    status = models.CharField(
        max_length=20,
        choices=[('Growing', 'Growing'), ('Harvested', 'Harvested')],
        default='Growing'
    )

    def __str__(self):
        return f"{self.crop.crop_name} - {self.start_date}"