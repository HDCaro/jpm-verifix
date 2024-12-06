from django.contrib.auth.models import User
from django.db import models


class Parameter(models.Model):
    compID = models.CharField(max_length=100, unique=True)
    product = models.CharField(
        max_length=100,
        choices=[
            ('FOR', 'FX Cash'), ('OPT', 'FX Options'),
            ('BASEMETALS', 'Basemetals'), ('ENERGY', 'Energy'),
            ('AGS', 'Agriculture'), ('INDEX', 'Indices')],
        default='FOR'  # Default product
    )
    value_date = models.DateField(null=True, blank=True)  # Allow NULL for existing rows
    security = models.CharField(max_length=100, blank=True, default='FXFORWARD')  # Default security
    notional = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)  # Default to 0
    currency_pair = models.CharField(max_length=100, blank=True, default='USD/EUR')  # Default pair
    side = models.CharField(
        max_length=1,
        choices=[('1', 'Buy'), ('2', 'Sell')],
        default='1'  # Default to Buy
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.id} - compID: {self.compID}, Product: {self.product}, Security: {self.security}"
