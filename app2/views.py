"""
Module: views.py
Author: Xihai Ren
Date: 2024-11-28
Description: Handles the chart data preparation and response for Practical Project Part 4.
"""
from collections import defaultdict
from django.shortcuts import render, redirect
from .forms import VehicleForm
from .file_io import load_data_from_csv, export_data_to_csv
from django.http import HttpResponse
from .dtos import VehicleInfoDTO
from django.core.paginator import Paginator
from django.http import JsonResponse, HttpResponseForbidden
import os
from .models import Vehicle, DBSettings   # Import the Settings model


vehicle_data = []  # List to store vehicle data in memory
next_id = 0  # Counter to generate unique row_id values for new vehicles
file_path = "app2/data/vehicles.csv"    # Path to the CSV file
load_count = 1000   # Number of vehicles to load from the CSV file

# Set the default storage method to in-memory if the setting is not already
storage_method = 'in_memory'  # Default storage method


def initialize_storage_method():
    """
    Initializes the storage method from the database, setting a default if not found.
    """
    global storage_method
    settings = DBSettings.objects.first()
    if settings:
        storage_method = settings.storage_method
    else:
        storage_method = 'in_memory'  # Default value if no settings record exists
        DBSettings.objects.create(storage_method=storage_method)


# Call the initializer once on module load
initialize_storage_method()


def load_vehicle_data():
    """
    Loads vehicle data from the CSV file or database based on the storage method.
    returns: vehicle_data: list of vehicle data
    """
    global next_id
    vehicle_data = []
    if storage_method == 'in_memory':
        vehicle_data = load_data_from_csv(file_path, load_count)
        next_id = len(vehicle_data)
    else:
        vehicle_data = list(Vehicle.objects.all()[:load_count])
        next_id = Vehicle.objects.count()

    return vehicle_data


def save_vehicle_data_to_db(vehicle_data):
    """
    Saves vehicle data to the CSV file or database based on the storage method.
    """
    if storage_method == 'in_memory':
        # export_data_to_csv(file_path, vehicle_data)
        print("Data saved to CSV file")
    else:
        for vehicle in vehicle_data:
            Vehicle.objects.create(
                model_year=vehicle.model_year,
                make=vehicle.make,
                model=vehicle.model,
                vehicle_class=vehicle.vehicle_class,
                engine_size=vehicle.engine_size,
                cylinders=vehicle.cylinders,
                transmission=vehicle.transmission,
                fuel_type=vehicle.fuel_type,
                city_fuel_efficiency=vehicle.city_fuel_efficiency,
                highway_fuel_efficiency=vehicle.highway_fuel_efficiency,
                combined_fuel_efficiency=vehicle.combined_fuel_efficiency,
                combined_mpg=vehicle.combined_mpg,
                co2_emissions=vehicle.co2_emissions,
                co2_rating=vehicle.co2_rating,
                smog_rating=vehicle.smog_rating
            )


def toggle_storage_method(request):
    """
    Toggles the storage method between memory and database.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: A redirect to the vehicle list view.
    """
    if request.method == 'POST':
        global storage_method, vehicle_data
        # Get the current storage method setting
        settings = DBSettings.objects.first()
        if settings is None:
            settings = DBSettings(storage_method='in_memory')
        else:
            settings.storage_method = 'in_memory' if settings.storage_method == 'database' else 'database'
        storage_method = settings.storage_method
        settings.save()
        vehicle_data = load_vehicle_data()
        return JsonResponse({'status': 'success', 'message': 'Storage method toggled'}, status=200)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)

    # return redirect('vehicle_list')


def vehicle_list(request):
    """
    Displays a list of all vehicles loaded from the CSV into memory.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered vehicle list page with data from memory.
    """
    global vehicle_data, next_id

    if not vehicle_data:  # If the data is not already loaded into memory
        # Load CSV data into memory (only if vehicle_data is empty)
        vehicle_data = load_vehicle_data()

     # Paginate the vehicle_data, showing 10 vehicles per page
    paginator = Paginator(vehicle_data, 10)  # 10 vehicles per page
    page_number = request.GET.get('page')
    # Get the vehicles for the current page
    page_obj = paginator.get_page(page_number)

    return render(request, 'app2/list_vehicle.html', {'vehicles': page_obj, 'storage_method': storage_method})


def add_vehicle(request):
    """
    Handles the creation of a new vehicle in memory.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered add vehicle form or a redirect to the list view.
    """
    global vehicle_data, next_id

    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            # Create a new VehicleInfoDTO object based on the form data
            next_id = next_id + 1

            if (storage_method == 'database'):
                new_vehicle = form.save()
                new_vehicle.row_id = next_id
                vehicle_data.append(new_vehicle)
            else:
                new_row_id = next_id
                new_vehicle = VehicleInfoDTO(
                    row_id=new_row_id,
                    model_year=form.data.get('model_year'),
                    make=form.data.get('make'),
                    model=form.data.get('model'),
                    vehicle_class=form.data.get('vehicle_class'),
                    engine_size=form.data.get('engine_size'),
                    cylinders=form.data.get('cylinders'),
                    transmission=form.data.get('transmission'),
                    fuel_type=form.data.get('fuel_type'),
                    city_l_per_100km=form.data.get('city_fuel_efficiency'),
                    highway_l_per_100km=form.data.get(
                        'highway_fuel_efficiency'),
                    combined_l_per_100km=form.data.get(
                        'combined_fuel_efficiency'),
                    combined_mpg=form.data.get('combined_mpg'),
                    co2_emissions_g_per_km=form.data.get('co2_emissions'),
                    co2_rating=form.data.get('co2_rating'),
                    smog_rating=form.data.get('smog_rating')
                )
                # Add new vehicle to in-memory list
                vehicle_data.append(new_vehicle)
            return redirect('vehicle_list')
    else:
        form = VehicleForm()
    return render(request, 'app2/add_vehicle.html', {'form': form})


def find_vehicle_by_id(row_id):
    """
    Finds a vehicle in memory by its row_id.

    Args:
        row_id (int): The row_id of the vehicle to find.

    Returns:
        VehicleInfoDTO: The vehicle with the specified row_id.
    """
    global vehicle_data
    if len(vehicle_data) == 0:
        vehicle_data = load_vehicle_data()
    for i in range(len(vehicle_data)):
        if vehicle_data[i].row_id == row_id:
            return i
    return None


def edit_vehicle(request, row_id):
    """
    Handles editing of an existing vehicle record in memory.

    Args:
        request (HttpRequest): The HTTP request object.
        index (int): The index of the vehicle in the in-memory list.

    Returns:
        HttpResponse: The rendered edit vehicle form or a redirect to the list view.
    """
    global vehicle_data

    if request.method == 'POST':
        form = VehicleForm(request.POST, instance=Vehicle())
        if form.is_valid():
            # Update the vehicle at the specified index
            index = find_vehicle_by_id(row_id)
            if index is None:
                return redirect('vehicle_list')
            if storage_method == 'database':
                form.instance.row_id = row_id
                vehicle = form.save()
                vehicle_data[index] = vehicle
            else:
                vehicle_data[index] = VehicleInfoDTO(
                    row_id=row_id,
                    model_year=form.data.get('model_year'),
                    make=form.data.get('make'),
                    model=form.data.get('model'),
                    vehicle_class=form.data.get('vehicle_class'),
                    engine_size=form.data.get('engine_size'),
                    cylinders=form.data.get('cylinders'),
                    transmission=form.data.get('transmission'),
                    fuel_type=form.data.get('fuel_type'),
                    city_l_per_100km=form.data.get('city_fuel_efficiency'),
                    highway_l_per_100km=form.data.get(
                        'highway_fuel_efficiency'),
                    combined_l_per_100km=form.data.get(
                        'combined_fuel_efficiency'),
                    combined_mpg=form.data.get('combined_mpg'),
                    co2_emissions_g_per_km=form.data.get('co2_emissions'),
                    co2_rating=form.data.get('co2_rating'),
                    smog_rating=form.data.get('smog_rating')
                )
            return redirect('vehicle_list')
    else:
        # Load the existing vehicle data for editing
        index = find_vehicle_by_id(row_id)
        if index is None:
            return redirect('vehicle_list')

        vehicle = vehicle_data[index]
        form = VehicleForm(initial={
            "row_id": vehicle.row_id,
            'model_year': vehicle.model_year,
            'make': vehicle.make,
            'model': vehicle.model,
            'vehicle_class': vehicle.vehicle_class,
            'engine_size': vehicle.engine_size,
            'cylinders': vehicle.cylinders,
            'transmission': vehicle.transmission,
            'fuel_type': vehicle.fuel_type,
            'city_fuel_efficiency': vehicle.city_fuel_efficiency,
            'highway_fuel_efficiency': vehicle.highway_fuel_efficiency,
            'combined_fuel_efficiency': vehicle.combined_fuel_efficiency,
            'combined_mpg': vehicle.combined_mpg,
            'co2_emissions': vehicle.co2_emissions,
            'co2_rating': vehicle.co2_rating,
            'smog_rating': vehicle.smog_rating
        })
    return render(request, 'app2/edit_vehicle.html', {'form': form, 'index': index})


def delete_vehicle(request, row_id):
    """
    Handles deletion of a vehicle record in memory.

    Args:
        request (HttpRequest): The HTTP request object.
        index (int): The index of the vehicle to be deleted.

    Returns:
        HttpResponse: A redirect to the vehicle list view after deletion.
    """
    global vehicle_data
    index = find_vehicle_by_id(row_id)
    if index is not None:
        if storage_method == 'database':
            vehicle = Vehicle.objects.get(row_id=row_id)
            vehicle.delete()
        del vehicle_data[index]
        return JsonResponse({'status': 'success', 'message': 'Vehicle deleted successfully'})
    return JsonResponse({'status': 'error', 'message': 'Vehicle not found'}, status=404)


def export_vehicles_to_csv(request):
    """
    Exports all vehicle data from memory to a CSV file and provides it as a downloadable response.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: A response with the downloadable CSV file.
    """
    exp_file_path = 'exported_vehicles.csv'
    export_data_to_csv(exp_file_path, vehicle_data)

    # Serve the file as a downloadable response
    with open(exp_file_path, 'rb') as f:
        response = HttpResponse(f.read(), content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename={
            os.path.basename(exp_file_path)}'
        return response


def reload_vehicles_from_csv(request):
    """
    Reloads all vehicle data from the CSV file into memory.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: A redirect to the vehicle list view.
    """
    global vehicle_data, next_id
    vehicle_data = load_data_from_csv(file_path, load_count)
    if storage_method == 'database':
        Vehicle.objects.all().delete()
        save_vehicle_data_to_db(vehicle_data)

    next_id = len(vehicle_data)
    # Return a JSON response to indicate success
    return JsonResponse({"status": "success", "message": "Data reloaded successfully"})


def view_vehicle(request, row_id):
    """
    Displays the details of a single vehicle.

    Args:
        request (HttpRequest): The HTTP request object.
        row_id (int): The row_id of the vehicle to view.

    Returns:
        HttpResponse: The rendered vehicle details page.
    """
    # global vehicle_data

    index = find_vehicle_by_id(row_id)
    if index is None:
        return HttpResponseForbidden("Vehicle not found")

    vehicle = vehicle_data[index]
    return render(request, 'app2/view_vehicle.html', {'vehicle': vehicle})


def charts(request):
    """
    Displays charts of the vehicle data.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered charts page.
    """
    global vehicle_data

    if not vehicle_data:  # If the data is not already loaded into memory
        # Load CSV data into memory (only if vehicle_data is empty)
        vehicle_data = load_vehicle_data()

    # Count the number of vehicles in each vehicle class
    # class_counts = {}
    # for vehicle in vehicle_data:
    #     if vehicle.vehicle_class in class_counts:
    #         class_counts[vehicle.vehicle_class] += 1
    #     else:
    #         class_counts[vehicle.vehicle_class] = 1

    # Get the selected dimension from the request parameters (default to 'vehicle_class')
    dimension = request.GET.get('dimension', None)
    is_ajax = False
    if dimension:
        is_ajax = True
    else:
        dimension = 'vehicle_class'

    # Create a dictionary to count the occurrences of the selected dimension
    class_counts = defaultdict(int)

    for vehicle in vehicle_data:
        # Get the value of the selected dimension (vehicle_class, make, model_year, etc.)
        dimension_value = getattr(vehicle, dimension, None)
        if dimension_value:
            class_counts[dimension_value] += 1

    # Prepare the data for the pie chart
    labels = list(class_counts.keys())
    counts = list(class_counts.values())

    # Check if the request is AJAX
    if is_ajax:
        # Return JSON data if the request is AJAX
        return JsonResponse({'labels': labels, 'counts': counts})

    # Render the full page with the chart if it's a normal request
    return render(request, 'app2/charts.html', {'class_counts': counts, 'labels': labels})
