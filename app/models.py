from django.db import models

# Create your models here.
class Event(models.Model):
    id = models.AutoField(primary_key=True)
    image=models.ImageField(upload_to="image")
    heading = models.CharField(max_length=100,  blank=True, null=True)
    caption=models.CharField(max_length=1000)
    booking_link = models.URLField(blank=True, null=True)
    def __str__(self):
        return self.heading

class RecentEvent(models.Model):
    id = models.AutoField(primary_key=True)
    image=models.ImageField(upload_to="recentimage")
    heading = models.CharField(max_length=100,  blank=True, null=True)
    caption=models.CharField(max_length=1000)
    
    def __str__(self):
        return self.heading
