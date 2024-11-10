import csv
from .dtos import VehicleInfoDTO  # Import the DTO class


def load_data_from_csv(file_path, limit=None):
    """
    Reads vehicle data from a CSV file and loads it into memory as VehicleInfoDTO objects.

    Args:
        file_path (str): The path to the CSV file.
        limit (int, optional): Maximum number of records to load. Defaults to None.

    Returns:
        list: A list of VehicleInfoDTO objects representing the vehicle data.
    """
    vehicles = []
    try:
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            count = 0

            # Read data and create VehicleInfoDTO objects
            for row in reader:
                vehicle = VehicleInfoDTO(
                    row_id=count+1,  # Assign a unique ID to each record
                    model_year=row['Model year'],
                    make=row['Make'],
                    model=row['Model'],
                    vehicle_class=row['Vehicle class'],
                    engine_size_l=row['Engine size (L)'],
                    cylinders=row['Cylinders'],
                    transmission=row['Transmission'],
                    fuel_type=row['Fuel type'],
                    city_l_per_100km=row['City (L/100 km)'],
                    highway_l_per_100km=row['Highway (L/100 km)'],
                    combined_l_per_100km=row['Combined (L/100 km)'],
                    combined_mpg=row['Combined (mpg)'],
                    co2_emissions_g_per_km=row['CO2 emissions (g/km)'],
                    co2_rating=row['CO2 rating'],
                    smog_rating=row['Smog rating']
                )
                vehicles.append(vehicle)  # Store the DTO object in the list

                count += 1
                if limit is not None and count >= limit:
                    break  # Exit if the limit is reached

    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")

    return vehicles  # Return the list of DTO objects


def export_data_to_csv(file_path, vehicles):
    """
    Exports vehicle data from in-memory DTOs to a CSV file.

    Args:
        file_path (str): The path where the CSV file will be saved.
        vehicles (list): A list of VehicleInfoDTO objects representing the vehicle data.
    """
    try:
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)

            # Write headers
            writer.writerow([
                'Model year', 'Make', 'Model', 'Vehicle class', 'Engine size (L)',
                'Cylinders', 'Transmission', 'Fuel type', 'City (L/100 km)',
                'Highway (L/100 km)', 'Combined (L/100 km)', 'Combined (mpg)',
                'CO2 emissions (g/km)', 'CO2 rating', 'Smog rating'
            ])

            # Write data from DTO objects
            for vehicle in vehicles:
                writer.writerow([
                    vehicle.model_year, vehicle.make, vehicle.model, vehicle.vehicle_class,
                    vehicle.engine_size_l, vehicle.cylinders, vehicle.transmission,
                    vehicle.fuel_type, vehicle.city_l_per_100km, vehicle.highway_l_per_100km,
                    vehicle.combined_l_per_100km, vehicle.combined_mpg, vehicle.co2_emissions_g_per_km,
                    vehicle.co2_rating, vehicle.smog_rating
                ])

        print(f"Data successfully exported to {file_path}")

    except IOError:
        print(f"Error: Could not write to file {file_path}")
