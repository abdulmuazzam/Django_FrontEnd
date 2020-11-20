from django.db import models

# Create your models here.



class Routines(models.Model):
    Name = models.CharField(max_length=30)
    x = models.FloatField()
    y = models.FloatField()
    z = models.FloatField()
    CapturedBy = models.CharField(max_length=30)

class Profile:
    ImgUrl: str
    Name: str
    Data : str

class Routine:

    def __init__(self, Name, Points, CapturedBy):
        self.Name = Name
        self.Points = Points
        self.CapturedBy = CapturedBy