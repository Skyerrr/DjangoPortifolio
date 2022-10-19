from django import forms
from . import models


class VehiclesForm(forms.ModelForm):
    class Meta:
        model = models.Vehicles
        fields = "__all__"


class GalleryForm(forms.ModelForm):
    class Meta:
        model = models.Gallery
        fields = "__all__"
