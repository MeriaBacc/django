from django.db import models



# Create your models here.
class Article(models.Model):
    Title = models.CharField(max_length=1000)
    Image = models.CharField(max_length=255)
    HeaderImage = models.CharField(max_length=255) 
    Introduction =  models.CharField(max_length=1000)
    Description = models.CharField(max_length=1000) 
    LastMod = models.DateField()
    Language = models.CharField(max_length=255) 
    KeyWords = models.CharField(max_length=1000)
    State = models.IntegerField()
    NumVisit = models.IntegerField()
    IdTheme = models.IntegerField()
    IdUser = models.IntegerField()
    IdHost = models.IntegerField()
