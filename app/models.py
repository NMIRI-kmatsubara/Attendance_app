from django.db import models

# Create your models here.
class Place(models.Model):
    pl = models.CharField(max_length=100)

    def __str__(self):
        return self.pl

class Atted_Person(models.Model):
    AP = models.CharField(max_length=100)



class Practice(models.Model):
    date = models.DateTimeField()
    manu = models.TextField(blank=True)
    Place_Category = models.ForeignKey(Place, on_delete=models.PROTECT)



