from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Parameter(models.Model):
    parameter1 = models.CharField(max_length=100, blank=True)
    parameter2 = models.CharField(max_length=100, blank=True)
    parameter3 = models.CharField(max_length=100, blank=True)
    parameter4 = models.CharField(max_length=100, blank=True)
    parameter5 = models.CharField(max_length=100, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + ' ' + self.user.username + ' - parameter1: ' + self.parameter1 + "..."
