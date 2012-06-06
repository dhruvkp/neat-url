from django.db import models

# Create your models here.
class Map(models.Model):
    tocken = models.CharField(max_length=10, unique=True)
    ourl = models.TextField()
    keywords = models.TextField()
    status = models.IntegerField()
