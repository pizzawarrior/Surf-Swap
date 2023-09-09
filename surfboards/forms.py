from django.forms import ModelForm
from surfboards.models import Surfboard, Reservation

# To be used with the view 'create_surfboard'
class SurfboardForm(ModelForm):
    class Meta:
        model = Surfboard
        fields = (
            "brand",
            "model",
            "type",
            "length",
            "width",
            "thickness",
            "volume",
            "style",
            "fin_style",
            "fin_system",
            "image",
            "currently_available",
            "description"

            )
