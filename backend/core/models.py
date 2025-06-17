from django.db import models

class DisasterEvent(models.Model):
    DISASTER_TYPES = [
        ('flood', 'Flood'),
        ('wildfire', 'Wildfire'),
        ('earthquake', 'Earthquake'),
        ('other', 'Other'),
    ]
    title = models.CharField(max_length=200)
    disaster_type = models.CharField(max_length=20, choices=DISASTER_TYPES)
    location = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    timestamp = models.DateTimeField()
    raw_data = models.JSONField()
    summary = models.TextField(blank=True)
    severity = models.FloatField(null=True, blank=True)