# Demonstration of what items() returns

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

print("1. The dictionary:")
print(user_0)
print()

print("2. What items() returns:")
print(user_0.items())
print()

print("3. Type of items():")
print(type(user_0.items()))
print()

print("4. Converting to list to see individual tuples:")
print(list(user_0.items()))
print()

print("5. Each tuple individually:")
for i, item in enumerate(user_0.items()):
    print(f"Item {i}: {item} (type: {type(item)})")
print()

print("6. Unpacking each tuple:")
for key, value in user_0.items():
    print(f"Key: '{key}' -> Value: '{value}'")

