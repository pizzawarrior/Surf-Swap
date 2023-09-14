from django.db import models
from django.contrib.auth.models import User


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
    borrower = models.ForeignKey(
        User,
        related_name='reservations',
        on_delete=models.CASCADE
    )


class Surfboard(models.Model):
    # Board types:
    Shortboard = 'Shortboard'
    Mid_length = 'Mid-length'
    Longboard = 'Longboard'

    # Board style:
    Fish = 'Fish'
    Twin = 'Twin'
    Round = 'Round'
    Asym = 'Asym'
    Swallow_tail = 'Swallow-tail'
    Pin_tail = 'Pin tail'
    Squash = 'Squash'
    Mini_simmons = 'Mini-simmons'
    Other = 'Other'

    # Fin Style:
    Single = 'Single fin'
    # twin = 'twin'
    Two_plus_one = '2+1'
    Thruster = 'Thruster'
    Quad = 'Quad'
    Five = 'Five-fin'
    Finless = 'Finless'
    # other = 'other

    # Fin System:
    Fcs1 = 'Fcs1'
    Fcs2 = 'Fcs2'
    Futures = 'Futures'
    # Other = 'other'

    # Format variables as tuples to be accessed in the model attributes
    BOARD_TYPES = [

        (Shortboard, 'Shortboard'),
        (Mid_length, 'Mid-length'),
        (Longboard, 'Longboard'),
        (Other, 'Other')
    ]

    TAIL_STYLE = [
        (Fish, 'Fish'),
        (Round, 'Round'),
        (Asym, 'Asym'),
        (Swallow_tail, 'Swallow-tail'),
        (Pin_tail, 'Pin tail'),
        (Squash, 'Squash'),
        (Other, 'Other')
    ]

    FIN_STYLE = [
        (Single, 'Single'),
        (Twin, 'Twin'),
        (Two_plus_one, '2+1'),
        (Thruster, 'Thruster'),
        (Quad, 'Quad'),
        (Five, 'Five-fin'),
        (Finless, 'Finless'),
        (Other, 'Other')
    ]

    FIN_SYSTEM = [
        (Fcs1, 'FCS 1'),
        (Fcs2, 'FCS 2'),
        (Futures, 'Futures'),
        (Other, 'Other')
    ]

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
    reservation = models.ForeignKey(
        Reservation,
        related_name='surfboards',
        on_delete=models.CASCADE, null=True
    )

    def __str__(self):
        return self.brand
