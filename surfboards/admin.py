from django.contrib import admin
from surfboards.models import Surfboard, Reservation

# Register your models here.
@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display= (
        'id',
        'surfboard',
        'owner',
        'borrower')


# Show CURRENT reservations:
@admin.register(Surfboard)
class SurfboardAdmin(admin.ModelAdmin):
    list_display= (
        'id',
        'owner',
        'make',
        'model',
        'currently_available'
        # count of surfboards would be cool
        # num boards currently loaned out
        # num boards currently borrowing
    )
