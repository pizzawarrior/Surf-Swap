from django.contrib import admin
from surfboards.models import Surfboard, Reservation


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display= (
        'id',
        # 'surfboards.surfboard',
        # 'surfboards.owner',
        'borrower',
        'type')


# Show CURRENT reservations:
@admin.register(Surfboard)
class SurfboardAdmin(admin.ModelAdmin):
    list_display= (
        'id',
        'owner',
        'brand',
        'model',
        'currently_available'
        # count of surfboards would be cool
        # num boards currently loaned out
        # num boards currently borrowing
    )
