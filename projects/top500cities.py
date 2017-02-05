import pandas as pd

cities = pd.read_csv('Top500_Indian_Cities.csv', header = 1)

#Top population counts for states
#cities.sort('population_total', ascending=False)[['state_name','population_total']]
state_population = cities.groupby(['state_name']).sum().sort_values('population_total', ascending = False).population_total
print state_population

#Top 10 cities with highest literacy rate
literacy_rate = cities.sort_values('effective_literacy_rate_total', ascending=False)[:10][['city','effective_literacy_rate_total']]
print literacy_rate

#Graduation rate; graduates over the total population
cities['graduate_percentage'] = cities.total_graduates/cities.population_total

#Graduation rate; graduates over the total population per state
gradrate = cities.groupby(['state_name']).sum().total_graduates/cities.groupby(['state_name']).sum().population_total
print gradrate

#List of states in order of the most number of cities in them
mostcities = cities.groupby(['state_name']).count().sort_values('city', ascending = False).city
print mostcities
