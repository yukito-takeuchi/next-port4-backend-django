from django.db import models

# Create your models here.
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=256)
    content = models.CharField(max_length=256)

    def __str__(self):
        return self.title

class Job(models.Model):    
    spot = models.CharField(max_length=100)
    rank = models.IntegerField()
    acucess = models.IntegerField()
    fun = models.IntegerField()
    many = models.IntegerField()
    view = models.IntegerField()