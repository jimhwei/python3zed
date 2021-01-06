#study drill 1
provinces = {
    'Ontario': 'ON',
    'British Columbia': 'BC',
    'Alberta': 'AB',
    'Quebec': 'QC'
}

# create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville',
    'ON': 'Ottawa',
    'BC': 'Vangcouver',
    'AB': 'Calgary'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'
cities['QC'] = 'Montreal'
cities['ON'] = 'Toronto'
#replaces the value in ontario

# print out some cities
print('-' * 10)
print("ON Province has: ", cities['ON'])
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

# print some states
print('-' * 10)
print("British Columbia's abbreviation is: ", provinces['British Columbia'])
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

# do it by using the state then cities dict
print('-' * 10)
print("Alberta has: ", cities[provinces['Alberta']])
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

# print every state abbreviation
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

#Canadian abbreviations based on dict provinces
print('-' * 10)
for province, abbrev in list(provinces.items()):
    print(f"{province} is abbreviated {abbrev}")

# print every city in state, now provinces too
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

# now do both at the same time (excl provinces)
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

#printing both cities and province for canadian
print('-' * 10)
for province, abbrev in list(provinces.items()):
    print(f"{province} province is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('-' * 10)
#safely get an abbreviation by state that might not be there
state_input = input('What state do you want to look up: ')
state = states.get(state_input)

if not state:
    print(f"Sorry, no {state_input}.")

#get a city with default value
city = cities.get(state_input, 'Does Not Exist')
print(f"The city for the state {state_input} is: {city}")

# best practice would be to use combine states and provinces as one entity
# this should've been two files
