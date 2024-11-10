

class VehicleInfoDTO:
    """
    Class to represent a vehicle information record. created by Xihai Ren
    """
    def __init__(self,row_id, model_year, make, model, vehicle_class, engine_size_l, cylinders, transmission, fuel_type,
                 city_l_per_100km, highway_l_per_100km, combined_l_per_100km, combined_mpg, co2_emissions_g_per_km,
                 co2_rating, smog_rating):
        """
        init method to initialize the object. created by Xihai Ren
        """
        self._row_id = row_id
        self._model_year = model_year
        self._make = make
        self._model = model
        self._vehicle_class = vehicle_class
        self._engine_size_l = engine_size_l
        self._cylinders = cylinders
        self._transmission = transmission
        self._fuel_type = fuel_type
        self._city_l_per_100km = city_l_per_100km
        self._highway_l_per_100km = highway_l_per_100km
        self._combined_l_per_100km = combined_l_per_100km
        self._combined_mpg = combined_mpg
        self._co2_emissions_g_per_km = co2_emissions_g_per_km
        self._co2_rating = co2_rating
        self._smog_rating = smog_rating

    # Accessors (getters)
    @property
    def row_id(self):
        """
        Method to get the row id. created by Xihai Ren
        """
        return self._row_id
    
    @property
    def model_year(self):
        """
        Method to get the model year. created by Xihai Ren
        """
        return self._model_year

    @property
    def make(self):
        """
        Method to get the make. created by Xihai Ren
        """
        return self._make

    @property
    def model(self):
        """
        Method to get the model. created by Xihai Ren
        """
        return self._model

    @property
    def vehicle_class(self):
        """
        Method to get the vehicle class. created by Xihai Ren
        """
        return self._vehicle_class

    @property
    def engine_size_l(self):
        """
        Method to get the engine size. created by Xihai Ren
        """
        return self._engine_size_l

    @property
    def cylinders(self):
        """
        Method to get the cylinders. created by Xihai Ren
        """
        return self._cylinders

    @property
    def transmission(self):
        """
        Method to get the transmission. created by Xihai Ren
        """
        return self._transmission

    @property
    def fuel_type(self):
        """
        Method to get the fuel type. created by Xihai Ren
        """
        return self._fuel_type

    @property
    def city_l_per_100km(self):
        """
        Method to get the city fuel consumption. created by Xihai Ren
        """
        return self._city_l_per_100km

    @property
    def highway_l_per_100km(self):
        """
        Method to get the highway fuel consumption. created by Xihai Ren
        """
        return self._highway_l_per_100km

    @property
    def combined_l_per_100km(self):
        """
        Method to get the combined fuel consumption. created by Xihai Ren
        """
        return self._combined_l_per_100km

    @property
    def combined_mpg(self):
        """
            Method to get the combined fuel consumption in mpg. created by Xihai Ren
        """
        return self._combined_mpg

    @property
    def co2_emissions_g_per_km(self):
        """    
            Method to get the CO2 emissions. created by Xihai Ren
        """
        return self._co2_emissions_g_per_km

    @property
    def co2_rating(self):
        """
            Method to get the CO2 rating. created by Xihai Ren
        """
        return self._co2_rating

    @property
    def smog_rating(self):
        """
            Method to get the smog rating. created by Xihai Ren
        """
        return self._smog_rating

    # Mutators (setters)
    @row_id.setter
    def row_id(self, value):
        """
        Method to set the row id. created by Xihai Ren
        """
        self._row_id = value
        
    @model_year.setter
    def model_year(self, value):
        """
        Method to set the model year. created by Xihai Ren
        """
        self._model_year = value

    @make.setter
    def make(self, value):
        """
        Method to set the make. created by Xihai Ren
        """
        self._make = value

    @model.setter
    def model(self, value):
        """
        Method to set the model. created by Xihai Ren
        """
        self._model = value

    @vehicle_class.setter
    def vehicle_class(self, value):
        """
        Method to set the vehicle class. created by Xihai Ren
        """
        self._vehicle_class = value

    @engine_size_l.setter
    def engine_size_l(self, value):
        """
        Method to set the engine size. created by Xihai Ren
        """
        self._engine_size_l = value

    @cylinders.setter
    def cylinders(self, value):
        """
        Method to set the cylinders. created by Xihai Ren
        """
        self._cylinders = value

    @transmission.setter
    def transmission(self, value):
        """
        Method to set the transmission. created by Xihai Ren
        """
        self._transmission = value

    @fuel_type.setter
    def fuel_type(self, value):
        """
        Method to set the fuel type. created by Xihai Ren
        """
        self._fuel_type = value

    @city_l_per_100km.setter
    def city_l_per_100km(self, value):
        """
        Method to set the city fuel consumption. created by Xihai Ren
        """
        self._city_l_per_100km = value

    @highway_l_per_100km.setter
    def highway_l_per_100km(self, value):
        """
        Method to set the highway fuel consumption. created by Xihai Ren
        """
        self._highway_l_per_100km = value

    @combined_l_per_100km.setter
    def combined_l_per_100km(self, value):
        """
        Method to set the combined fuel consumption. created by Xihai Ren
        """
        self._combined_l_per_100km = value

    @combined_mpg.setter
    def combined_mpg(self, value):
        """
        Method to set the combined fuel consumption in mpg. created by Xihai Ren
        """
        self._combined_mpg = value

    @co2_emissions_g_per_km.setter
    def co2_emissions_g_per_km(self, value):
        """
        Method to set the CO2 emissions. created by Xihai Ren
        """
        self._co2_emissions_g_per_km = value

    @co2_rating.setter
    def co2_rating(self, value):
        """
        Method to set the CO2 rating. created by Xihai Ren
        """
        self._co2_rating = value

    @smog_rating.setter
    def smog_rating(self, value):
        """
        Method to set the smog rating. created by Xihai Ren
        """
        self._smog_rating = value

    def display(self):
        """
        Method to display the record. created by Xihai Ren
        """
        print(f"Model Year: {self._model_year}")
        print(f"Make: {self._make}")
        print(f"Model: {self._model}")
        print(f"Vehicle Class: {self._vehicle_class}")
        print(f"Engine Size (L): {self._engine_size_l}")
        print(f"Cylinders: {self._cylinders}")
        print(f"Transmission: {self._transmission}")
        print(f"Fuel Type: {self._fuel_type}")
        print(f"City (L/100km): {self._city_l_per_100km}")
        print(f"Highway (L/100km): {self._highway_l_per_100km}")
        print(f"Combined (L/100km): {self._combined_l_per_100km}")
        print(f"Combined (mpg): {self._combined_mpg}")
        print(f"CO2 Emissions (g/km): {self._co2_emissions_g_per_km}")
        print(f"CO2 Rating: {self._co2_rating}")
        print(f"Smog Rating: {self._smog_rating}")
        # print("\n")
