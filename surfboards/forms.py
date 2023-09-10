from django.forms import ModelForm
from django import forms
from surfboards.models import Surfboard

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
            "description"
            )

        # Use widgets for dropdowns. See .models for how these were setup
        widgets = {
            'type': forms.Select(attrs={'class': 'form-control'}),
            'style': forms.Select(attrs={'class': 'form-control'}),
            'fin_style': forms.Select(attrs={'class': 'form-control'}),
            'fin_system': forms.Select(attrs={'class': 'form-control'}),
        }
