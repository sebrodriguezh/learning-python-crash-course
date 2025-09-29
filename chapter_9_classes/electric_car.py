class Car:
    """A class to represent a car with its specifications and mileage tracking."""

    def __init__(self, make, model, year):
        """Initialize car attributes.
        
        Args:
            make (str): The manufacturer of the car
            model (str): The model of the car
            year (int): The year the car was manufactured
        """
        self.make = make
        self.model = model
        self.year = year
        self.mileage = 0
    
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name of the car.
        
        Returns:
            str: A formatted string containing year, make, and model
        """
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Display the car's current mileage."""
        print(f"This car has {self.mileage} miles on it.")
    
    def update_odometer(self, new_mileage):
        """Set the odometer reading to the given value.
        
        Reject the change if it attempts to roll the odometer back.
        
        Args:
            new_mileage (int): The new mileage value to set
        """
        if new_mileage >= self.mileage:
            self.mileage = new_mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles_driven):
        """Add the given amount to the current mileage.
        
        Args:
            miles_driven (int): Number of miles to add to the odometer
        """
        self.mileage += miles_driven

class Battery:
    """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size=40):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")
    
    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        print(f"This car can go about {range} miles on a full charge.")


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class.
        Then initialize attribuites specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()