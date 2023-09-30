from django.db import models
from django.contrib.auth.models import User
from .model_choices import BOARD_TYPES, TAIL_STYLE, FIN_STYLE, FIN_SYSTEM


class Surfboard(models.Model):

    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100, null=True)
    type = models.CharField('Board Type', max_length=20, blank=False, choices=BOARD_TYPES)
    # Change this to length FEET:
    length = models.DecimalField(max_digits=6, decimal_places=2)
    # Add length INCHES
    width = models.DecimalField(max_digits=6, decimal_places=2)
    # Add width fraction
    thickness = models.FloatField(max_length=4)
    volume = models.DecimalField('Volume, L', max_digits=3, decimal_places=1)
    style = models.CharField('Tail Style', max_length=100, blank=False, choices=TAIL_STYLE)
    fin_style = models.CharField('Fin Style', max_length=20, blank=False, choices=FIN_STYLE)
    fin_system = models.CharField('Fin System', max_length=20, blank=False, choices=FIN_SYSTEM)
    image = models.URLField(blank=True)
    currently_available = models.BooleanField(default=True)
    description = models.TextField(max_length=1000)
    owner = models.ForeignKey(
        User,
        related_name='surfboards',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.brand


class Reservation(models.Model):
    # Reservation length:
    Two_weeks = '2 weeks'
    One_month = '1 month'
    Other = 'Other'

    RESERVATION_TYPE = [
        (Two_weeks, '2 weeks'),
        (One_month, '1 month'),
        (Other, 'Other')
    ]

    created_on = models.DateTimeField(auto_now_add=True)
    type = models.CharField('Reservation Length', max_length=100, blank=False, choices=RESERVATION_TYPE)
    notes = models.TextField(max_length=1000, null=True)
    # Borrower should be user (NOT FOREIGN KEY)
    borrower = models.ForeignKey(
        User,
        related_name='reservations',
        on_delete=models.CASCADE
    )
    surfboard = models.ForeignKey(
        'Surfboard',
        related_name='surfboards',
        on_delete=models.CASCADE,
        null=True
    )
