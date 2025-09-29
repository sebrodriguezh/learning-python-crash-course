def city_country(city_name, city_country):
    formatted_city = city_name.title()
    formatted_country = city_country.title()

    formated_string = f"{formatted_city}, {formatted_country}"
    return formated_string

formated_city = city_country('santiago', 'chile')
print(formated_city)