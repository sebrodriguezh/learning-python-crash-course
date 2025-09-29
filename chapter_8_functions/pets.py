def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='harry')

def make_shirt(size='Large', text_message='I love Python'):
    """Display the size and text message that it's going to be printed on a shirt"""
    print(f"\nThe size of the shirt is {size.upper()}.")
    print(f"The message that will be displayed is '{text_message}'.")

make_shirt()
make_shirt(size='medium)