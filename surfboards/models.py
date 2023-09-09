from django.db import models
from django.contrib.auth.models import User


class Reservation(models.Model):
    borrower = models.ForeignKey(
        User,
        related_name='reservation',
        on_delete=models.CASCADE
    )


class Surfboard(models.Model):
    brand = models.CharField(max_length=100)
    model = models.TextField(max_length=100, null=True)
    type = models.CharField(max_length=25)
    length = models.DecimalField(max_digits=6, decimal_places=2)
    width = models.DecimalField(max_digits=5, decimal_places=2)
    thickness = models.DecimalField(max_digits=3, decimal_places=2)
    volume = models.DecimalField(max_digits=3, decimal_places=2)
    style = models.CharField(max_length=100)
    fin_style = models.CharField(max_length=50)
    fin_system = models.CharField(max_length=50)
    image = models.URLField(blank=True)
    currently_available = models.BooleanField(default=False)
    owner = models.ForeignKey(
        User,
        related_name='surfboards',
        on_delete=models.CASCADE
    )
    reservation = models.ForeignKey(
        Reservation,
        related_name='surfboards',
        on_delete=models.CASCADE, null=True
    )

    def __str__(self):
        return self.brand
