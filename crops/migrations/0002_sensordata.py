# Generated by Django 5.1.7 on 2025-04-01 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crops', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SensorData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tds', models.FloatField()),
                ('ph', models.FloatField()),
                ('humidity', models.FloatField()),
                ('water_temp', models.FloatField()),
                ('air_temp', models.FloatField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
