from django.db import models

# Create your models here.
from django.db import models


class Vehicle(models.Model):
    """
    Vehicle model represents various attributes of a vehicle,
    matching the fields from the provided dataset.
    """
    row_id = models.AutoField(primary_key=True)
    """Unique identifier for the vehicle record with auto-increment."""

    model_year = models.IntegerField()
    """Year the vehicle was manufactured."""

    make = models.CharField(max_length=100)
    """Manufacturer of the vehicle."""

    model = models.CharField(max_length=100)
    """Model of the vehicle."""

    vehicle_class = models.CharField(max_length=100)
    """Vehicle class/category."""

    engine_size = models.DecimalField(max_digits=4, decimal_places=1)
    """Engine size in liters."""

    cylinders = models.IntegerField()
    """Number of engine cylinders."""

    transmission = models.CharField(max_length=50)
    """Type of transmission."""

    fuel_type = models.CharField(max_length=50)
    """Type of fuel used by the vehicle."""

    city_fuel_efficiency = models.DecimalField(max_digits=4, decimal_places=2)
    """Fuel efficiency in the city (in liters per 100 km)."""

    highway_fuel_efficiency = models.DecimalField(
        max_digits=4, decimal_places=2)
    """Fuel efficiency on highways (in liters per 100 km)."""

    combined_fuel_efficiency = models.DecimalField(
        max_digits=4, decimal_places=2)
    """Combined fuel efficiency (in liters per 100 km)."""

    combined_mpg = models.IntegerField()
    """Combined fuel efficiency in miles per gallon (mpg)."""

    co2_emissions = models.IntegerField()
    """CO2 emissions in grams per kilometer."""

    co2_rating = models.IntegerField()
    """CO2 emission rating."""

    smog_rating = models.IntegerField()
    """Smog emission rating."""

    def __str__(self):
        """
        Returns a string representation of the vehicle instance.
        """
        return f"{self.model_year} {self.make} {self.model}"


class DBSettings(models.Model):
    """
    Model to store application settings.
    """

    STORAGE_METHOD_CHOICES = [
        ('in_memory', 'In Memory'),
        ('database', 'Database'),
    ]
    """Choices for the storage method field."""

    storage_method = models.CharField(
        max_length=20,
        choices=STORAGE_METHOD_CHOICES,
        default='in_memory',
    )
    """Storage method for vehicle data."""

    def __str__(self):
        """
        Returns a string representation of the settings instance.
        """
        return f"Settings: {self.storage_method}"
