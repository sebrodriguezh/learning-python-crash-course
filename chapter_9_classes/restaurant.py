class Restaurant:
    """A class to represent a restaurant with its basic information and customer tracking."""
    
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant attributes.
        
        Args:
            restaurant_name (str): The name of the restaurant
            cuisine_type (str): The type of cuisine served
        """
        self.name = restaurant_name
        self.cuisine_type = cuisine_type
        self.customers_served = 0
    
    def describe_restaurant(self):
        """Display a description of the restaurant including name and cuisine type."""
        print(f"The restaurant is called {self.name}.")
        print(f"It's a {self.cuisine_type} restaurant.")
    
    def open_restaurant(self):
        """Display a message indicating the restaurant is open for business."""
        print(f"The {self.name} is open!")
    
    def set_customers_served(self, customer_count):
        """Set the number of customers served to a specific value.
        
        Args:
            customer_count (int): The number of customers to set
        """
        self.customers_served = customer_count
    
    def increment_customers_served(self, additional_customers):
        """Add to the current number of customers served.
        
        Args:
            additional_customers (int): Number of additional customers served
        """
        self.customers_served += additional_customers 


restaurant = Restaurant("Tony's Pizza", "italian")
print(restaurant.name)
print(restaurant.cuisine_type)
print(restaurant.customers_served)

restaurant.set_customers_served(15)
print(restaurant.customers_served)

restaurant.increment_customers_served(25)
print(restaurant.customers_served)

restaurant.describe_restaurant()
restaurant.open_restaurant()
        