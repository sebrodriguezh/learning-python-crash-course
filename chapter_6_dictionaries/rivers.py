rivers = {
    'nile': 'egypt',
    'yangtse': 'china', 
    'amazon': 'peru',
}

for river, country in rivers.items():
    print(f'\nThe {river.title()} runs through {country.title()}')

for river in rivers.keys():
    print(river.title())

for country in rivers.values():
    print(country.title())