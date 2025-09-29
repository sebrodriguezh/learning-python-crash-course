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

my_used_car = Car('subaru', 'outback', 2019)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()