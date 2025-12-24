from django.db import models
from django.contrib.auth.models import User

class events(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    location = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title
    
class Registration(models.Model):
    events = models.ForeignKey(events,
        on_delete=models.CASCADE,
        related_name='registration'
    )
    name = models.CharField(max_length=100)
    email = models.EmailField()
    registered_at = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.name
  
