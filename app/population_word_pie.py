import population
import charts
import pandas as pd

def test(iter):
    perce = []
    country = []
    for value in iter:
        perce.append(value['World Population Percentage'])
        country.append(value['Country/Territory'])
    res = dict(zip(country, perce))    
    return res.keys(), res.values()
        

def run():
    df = pd.read_csv('./world_population.csv')
    df = df[df['Continent']=='Africa']
    countries = df['Country/Territory'].values
    percentages = df['World Population Percentage'].values
    # keys, values = test(iter)
    charts.generate_pie_chart(countries, percentages)
    

if __name__=='__main__':
    run()