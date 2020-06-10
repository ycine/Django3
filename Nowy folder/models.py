from django.db import models


class Model1(models.Model):
    id = models.BigIntegerField(primary_key=True)
    imie = models.CharField(max_length=20)
    nazwisko = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)

    def __unicode__(self):
        return self.imie