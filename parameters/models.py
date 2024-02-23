from django.db import models


# Create your models here.


class Parameter(models.Model):
    compID = models.CharField(max_length=100, unique=True)
    parameter1 = models.CharField(max_length=100, blank=True)
    parameter2 = models.CharField(max_length=100, blank=True)
    parameter3 = models.CharField(max_length=100, blank=True)
    parameter4 = models.CharField(max_length=100, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(
            self.id) + ' - compID: ' + self.compID + " parameters: " + self.parameter1 + '/' + self.parameter2 + '/' + self.parameter3 + '/' + self.parameter4
