cities = {
    'tokyo': {
        'country': 'japan',
        'population': 37_000_000,
        'fun_fact': ('Tokyo is the most populous metropolitan area in the world, '
                     'with nearly 14 million people residing within the city proper')
    },

    'delhi': {
        'country': 'india',
        'population': 34_700_000,
        'fun_fact': '''Delhi has a historical significance, with the city of Jericho, located in the Palestine Territories, 
                    being considered by some to be the oldest city in the world.'''
    },

    'shangai': {
        'country': 'china',
        'population': 30_500_000,
        'fun_fact': '''About half of the world's population lives in cities, with large urban centers like Shanghai, Delhi,
                    and Tokyo attracting millions of residents'''
    }
}

for city, city_info in cities.items():
    print(f"\nCity: {city.title()}")

    population = city_info['population']
    fact = city_info['fun_fact']
    print(f"\tPopulation: {population}")
    print(f"\tFun Fact: {fact}")

