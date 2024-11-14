from django.test import TestCase, Client
from django.urls import reverse
from app2.views import vehicle_data
from .models import Vehicle, DBSettings
from .file_io import load_data_from_csv

class VehicleTests(TestCase):
    """ Test cases created by Xihai Ren"""

    def setUp(self):
        """
        Set up test data and environment before each test.
        """
        self.client = Client()  # Django test client
        self.vehicle_data = {
            "row_id": 1,
            'model_year': 2020,
            'make': 'Toyota',
            'model': 'Camry',
            'vehicle_class': 'Sedan',
            'engine_size': 2.5,
            'cylinders': 4,
            'transmission': 'Automatic',
            'fuel_type': 'Gasoline',
            'city_fuel_efficiency': 7.5,
            'highway_fuel_efficiency': 6.0,
            'combined_fuel_efficiency': 6.8,
            'combined_mpg': 34,
            'co2_emissions': 200,
            'co2_rating': 5,
            'smog_rating': 3
        }
        # Create initial database setting if it does not exist
        DBSettings.objects.create(storage_method='database')

    def test_initialize_storage_method(self):
        """
        Test that the storage method initializes correctly based on DBSettings.
        """
        settings = DBSettings.objects.first()
        self.assertEqual(settings.storage_method, 'database')
        print('Initialize storage method test passed created by Xihai Ren.')

    def test_toggle_storage_method(self):
        """
        Test toggling the storage method between 'in_memory' and 'database'.
        """
        response = self.client.post(reverse('toggle_storage_method'))
        self.assertEqual(response.status_code, 200)
        settings = DBSettings.objects.first()
        self.assertEqual(settings.storage_method, 'in_memory')

        # Toggle back to in_memory
        response = self.client.post(reverse('toggle_storage_method'))
        self.assertEqual(response.status_code, 200)
        settings = DBSettings.objects.first()
        self.assertEqual(settings.storage_method, 'database')
        print('Toggle storage method test passed created by Xihai Ren.')

    def test_add_vehicle(self):
        """
        Test adding a new vehicle to the system.
        """
        response = self.client.post(
            reverse('add_vehicle'), data=self.vehicle_data)
        self.assertEqual(response.status_code, 302)  # Redirects after success

        global vehicle_data
        self.assertTrue(any(v.model == 'Camry' for v in vehicle_data))
        print('Add vehicle test passed created by Xihai Ren.')

    def test_edit_vehicle(self):
        """
        Test editing an existing vehicle.
        """
        # Create a new vehicle for testing
        vehicle = Vehicle.objects.create(**self.vehicle_data)

        # Prepare data for editing
        edited_data = self.vehicle_data.copy()
        edited_data['model'] = 'Corolla'

        # Edit vehicle
        response = self.client.post(reverse('edit_vehicle', args=[vehicle.row_id]), data=edited_data)
        self.assertEqual(response.status_code, 302)

        # Verify that the model is updated
        updated_vehicle = Vehicle.objects.get(row_id=vehicle.row_id)
        self.assertEqual(updated_vehicle.model, 'Corolla')
        print('Edit vehicle test passed created by Xihai Ren.')


    def test_delete_vehicle(self):
        """
        Test deleting a vehicle.
        """
        # Create a new vehicle for testing
        vehicle = Vehicle.objects.create(**self.vehicle_data)

        # Delete the vehicle
        response = self.client.post(reverse('delete_vehicle', args=[vehicle.row_id]))
        self.assertEqual(response.status_code, 200)

        # Verify that the vehicle has been deleted
        with self.assertRaises(Vehicle.DoesNotExist):
            Vehicle.objects.get(row_id=vehicle.row_id)
        print('Delete vehicle test passed created by Xihai Ren.')


    def test_export_vehicles_to_csv(self):
        """
        Test exporting vehicles to a CSV file.
        """
        # Add a vehicle to export
        Vehicle.objects.create(**self.vehicle_data)

        response = self.client.get(reverse('export_vehicles_to_csv'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'text/csv')
        print('Export vehicles to CSV test passed created by Xihai Ren.')

    def test_reload_vehicles_from_csv(self):
        """
        Test reloading vehicles from the CSV file.
        """
        # Pre-load data into CSV for testing reload
        load_data_from_csv('app2/data/vehicles.csv', 1000)  # Adjust path if needed

        response = self.client.get(reverse('reload_vehicles_from_csv'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get("status"), "success")
        print('Reload vehicles from CSV test passed created by Xihai Ren.')