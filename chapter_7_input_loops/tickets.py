prompt = "\nWelcome to Moe Joey's Movie Theater. Please, enter your age for discounts."



while True:
    age = int(input(prompt))

    if age < 3:
        print("Your ticket is free!")
    elif age < 13:
        print("Your ticket is $10")
    else:
        print("Youre ticket is $15")