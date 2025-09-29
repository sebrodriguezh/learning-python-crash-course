def make_sandwich(*ingredients):
    """Summarize the sandwich we are about to make."""
    print(f"\nMaking a sandwich with the following toppings:")
    for ingredient in ingredients:
        print(f"- {ingredient.title()}")

make_sandwich('ham', 'cheese', 'pickles')