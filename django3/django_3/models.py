from django.db import models
# Create your models here.

class Model1(models.Model):
    numer = models.BigIntegerField()
    imie = models.CharField(max_length=20)
    nazwisko = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)

    def __unicode__(self):
        return self.imie