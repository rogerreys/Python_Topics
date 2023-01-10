import utils

data = [
        {
        'Country': 'Colombia',
        'Population':300
        },
        {
        'Country': 'Bolivia',
        'Population':300
        },
    ]

def run():
    key, val = utils.get_population()
    print(key, val)

    country = input("Type country=>\n")

    print(utils.population_by_country(data, country.title()))  

# Se puede 
if __name__ == '__main__':
    run()