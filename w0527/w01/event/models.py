from django.db import models
from datetime import datetime
# Create your models here.
class Event(models.Model):
    no = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    startdate = models.DateField()
    enddate = models.DateField()
    rdate = models.DateTimeField(default=datetime.now(),blank=True)
    
    def __str__(self):
        return f"{self.no},{self.title}"