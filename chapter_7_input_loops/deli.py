sandwich_oders = ['pastrami', 'meat', 'cheese', 'pastrami', 'pastrami', 'pastrami']

finished_sandwiches = []

print("The deli has run out of pastrami")
while 'pastrami' in sandwich_oders:
    sandwich_oders.remove('pastrami')

while sandwich_oders:

    unfinished_sandwich = sandwich_oders.pop()

    print(f"I made your {unfinished_sandwich} sandwich.")

    finished_sandwiches.append(unfinished_sandwich)

for sandwich in finished_sandwiches:
    print(f"I made your {sandwich} sandwich.")
