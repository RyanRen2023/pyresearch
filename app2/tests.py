from django.test import TestCase
from django.urls import reverse
from app2.views import vehicle_data, next_id

# Create your tests here.
class add_vehicle_test(TestCase):
    """ Test cases for the add_vehicle view  created by Xihai Ren"""
    def setUp(self) -> None:
        """Set up the test case by clearing the vehicle_data list and resetting the next_id counter."""
        global vehicle_data, next_id
        vehicle_data.clear()
        next_id = 0

    def test_add_vehicle(self):
        """Test that a new vehicle can be added to the in-memory list."""
        post_data = {
            'model_year': 2020,
            'make': 'Toyota',
            'model': 'Corolla',
            'vehicle_class': 'Compact',
            'engine_size': 2.0,
            'cylinders': 4,
            'transmission': 'Automatic',
            'fuel_type': 'Gasoline',
            'city_fuel_efficiency': 7.5,
            'highway_fuel_efficiency': 5.5,
            'combined_fuel_efficiency': 6.5,
            'combined_mpg': 40,
            'co2_emissions': 150,
            'co2_rating': 5,
            'smog_rating': 7
        }

        response = self.client.post(reverse('add_vehicle'), post_data) # Send a POST request to the add_vehicle view
        # print(respnse)
        self.assertEqual(len(vehicle_data), 1) # Check that the vehicle was added to the in-memory list
        new_vehicle = vehicle_data[0] # Get the new vehicle from the in-memory list

        self.assertEqual(new_vehicle.model_year, '2020') # Check that the vehicle data matches the form data
        self.assertEqual(new_vehicle.make, 'Toyota')
        self.assertEqual(new_vehicle.model, 'Corolla')
        self.assertEqual(new_vehicle.vehicle_class, 'Compact')
        self.assertEqual(new_vehicle.engine_size_l, '2.0')
        self.assertEqual(new_vehicle.cylinders, '4')
        self.assertEqual(new_vehicle.transmission, 'Automatic')
        self.assertEqual(new_vehicle.fuel_type, 'Gasoline')
        self.assertEqual(new_vehicle.city_l_per_100km, '7.5')
        self.assertEqual(new_vehicle.highway_l_per_100km, '5.5')
        self.assertEqual(new_vehicle.combined_l_per_100km, '6.5')
        self.assertEqual(new_vehicle.combined_mpg, '40')
        self.assertEqual(new_vehicle.co2_emissions_g_per_km, '150')
        self.assertEqual(new_vehicle.co2_rating, '5')
        self.assertEqual(new_vehicle.smog_rating, '7')
        print('test_add_vehicle, created by Xihai Ren')



# class VehicleViewTest(TestCase):
#     def test_vehicle_list(self):
#         print('test_vehicle_list, created by Xihai Ren')
#         response = self.client.get(reverse('vehicle_list'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'app2/list_vehicle.html')

#     def test_add_vehicle(self):
#         print('test_add_vehicle, created by Xihai Ren')
#         response = self.client.get(reverse('add_vehicle'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'app2/add_vehicle.html')

#     def test_edit_vehicle(self):
#         # import pdb; pdb.set_trace()
#         print('test_edit_vehicle, created by Xihai Ren')
#         url = reverse('edit_vehicle', args=[1])
#         print(url)
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'app2/edit_vehicle.html')

#     def test_delete_vehicle(self):
#         print('test_delete_vehicle, created by Xihai Ren')
#         response = self.client.get(reverse('delete_vehicle', args=[2]))
#         self.assertEqual(response.status_code, 200)

#     def test_export_vehicles_to_csv(self):
#         print('test_export_vehicles_to_csv, created by Xihai Ren')
#         response = self.client.get(reverse('export_vehicles_to_csv'))
#         self.assertEqual(response.status_code, 200)

#     def test_reload_vehicles_from_csv(self):
#         print('test_reload_vehicles_from_csv, created by Xihai Ren')
#         response = self.client.get(reverse('reload_vehicles_from_csv'))
#         self.assertEqual(response.status_code, 200)

#     def test_view_vehicle(self):
#         print('test_view_vehicle, created by Xihai Ren')
#         response = self.client.get(reverse('view_vehicle', args=[1]))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'app2/view_vehicle.html')
