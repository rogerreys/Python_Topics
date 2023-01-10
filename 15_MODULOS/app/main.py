import utils

key, val = utils.get_population()
print(key, val)


countries = [
    {
    'Country': 'Colombia',
    'Population':300
    },
    {
    'Country': 'Bolivia',
    'Population':300
    },
]

country = input("Type country=>\n")

print(utils.population_by_country(countries, country.title()))