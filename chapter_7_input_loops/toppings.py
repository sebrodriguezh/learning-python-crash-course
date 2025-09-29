prompt = "\nPlease enter the pizza toppings you want. "
prompt += "\n(Enter 'quit' when you're finished.)"

while True:
    toppings = input(prompt)

    if toppings == 'quit':
        break
    else:
        print(f"What a great choice {toppings.title()} is!")