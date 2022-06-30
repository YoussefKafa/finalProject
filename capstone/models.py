from django.db import models
from datetime import datetime

class Subscription (models.Model):
    email=models.EmailField()

class Inbox(models.Model):
    date = models.DateTimeField(default=datetime.now())
    name= models.CharField(max_length=30)
    email=models.EmailField()
    subject=models.CharField(max_length=50)
    message=models.CharField(max_length=2000)