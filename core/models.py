from django.db import models

# Create your models here.
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=256)
    content = models.CharField(max_length=256)

    def __str__(self):
        return self.title

class Job(models.Model):    
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    def __str__(self):
        return self.title