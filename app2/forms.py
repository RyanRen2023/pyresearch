from django import forms
from .models import Vehicle

class VehicleForm(forms.ModelForm):
    """
    A form for creating and editing vehicle records, using the Vehicle model.
    """
    class Meta:
        model = Vehicle
        fields = [
            'row_id','model_year', 'make', 'model', 'vehicle_class', 'engine_size',
            'cylinders', 'transmission', 'fuel_type', 'city_fuel_efficiency', 
            'highway_fuel_efficiency', 'combined_fuel_efficiency', 'combined_mpg', 
            'co2_emissions', 'co2_rating', 'smog_rating'
        ]

        widgets = {
            'row_id': forms.HiddenInput(),
        }