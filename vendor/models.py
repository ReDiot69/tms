from django.db import models


class Vendor(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=25)
    number = models.IntegerField()

    def __str__(self):
        return self.name
