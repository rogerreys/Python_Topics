import population
import charts

def test(iter):
    perce = []
    country = []
    for value in iter:
        perce.append(value['World Population Percentage'])
        country.append(value['Country/Territory'])
    res = dict(zip(country, perce))    
    return res.keys(), res.values()
        

def run():
    iter = population.convert('./world_population.csv')
    keys, values = test(iter)
    charts.generate_pie_chart(keys, values)

    

if __name__=='__main__':
    run()