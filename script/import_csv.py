import os
from app2.file_io import load_data_from_csv
from app2.models import Vehicle
from django.conf import settings


def import_csv_to_db():
    csv_file_path = os.path.join(settings.BASE_DIR, 'data', 'vehicles.csv')
    print(csv_file_path)
    vehicles = load_data_from_csv(csv_file_path)
    print(len(vehicles))
    for dto in vehicles:
        # Create a Vehicle instance directly using Vehicle.objects.create
        # print(dto)
        Vehicle.objects.create(
            model_year=dto.model_year,
            make=dto.make,
            model=dto.model,
            vehicle_class=dto.vehicle_class,
            engine_size=dto.engine_size,
            cylinders=dto.cylinders,
            transmission=dto.transmission,
            fuel_type=dto.fuel_type,
            city_fuel_efficiency=dto.city_l_per_100km,
            highway_fuel_efficiency=dto.highway_l_per_100km,
            combined_fuel_efficiency=dto.combined_l_per_100km,
            combined_mpg=dto.combined_mpg,
            co2_emissions=dto.co2_emissions_g_per_km,
            co2_rating=dto.co2_rating,
            smog_rating=dto.smog_rating
        )
