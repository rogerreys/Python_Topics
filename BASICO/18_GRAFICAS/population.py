import csv
import matplotlib.pyplot as plt
import charts

def convert(path):
    with open(path, 'r') as file:
        text = csv.reader(file, delimiter=',')
        head = next(text)
        result = []
        for row in text:
            iter = list(zip(head, row))
            data_value = {key:value for key, value in iter if (
                key in('Rank','CCA3', 'Country/Territory','Capital','Continent',
                '2022 Population','2020 Population','2015 Population', '2010 Population',
                '2000 Population','1990 Population', '1980 Population', '1970 Population',
                'World Population Percentage')
            )}
            result.append(data_value)
        
        return result

def population(country, iterable):
    country_data = list(filter(lambda x:x['Country/Territory']==country, iterable))[0]
    
    population_dict = {
        '2022': int(country_data['2022 Population']),
        '2020': int(country_data['2020 Population']),
        '2015': int(country_data['2015 Population']),
        '2010': int(country_data['2010 Population']),
        '2000': int(country_data['2000 Population']),
        '1990': int(country_data['1990 Population']),
        '1980': int(country_data['1980 Population']),
        '1970': int(country_data['1970 Population'])
    }
    return population_dict.keys(), population_dict.values()

def run_population():
    res = convert('./world_population.csv')
    key, values = population("Ecuador", res)
    charts.generate_bar_chart(key, values)
    
    

if __name__=='__main__':
    run_population()