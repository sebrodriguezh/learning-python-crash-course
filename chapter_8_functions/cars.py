def make_car(manufacturer, model_name, **cars):
    """Create a dictionary with the details of a car"""
    cars['manufacturer'] = manufacturer
    cars['model'] = model_name

    return cars

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)
