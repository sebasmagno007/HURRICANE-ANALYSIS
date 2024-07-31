# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}
def conversion_float(the_list, conversion):
  updated_list = []
  for i in the_list:
    if i == 'Damages not recorded':
      updated_list.append('Damages not recorded')
    else:
      for a in i:
        if a == "M":
          num = int(float(i[:-1]) * conversion["M"])
        elif a == "B":
          num = int(float(i[:-1]) * conversion["B"])
      updated_list.append(num)
  return updated_list
# test function by updating damages
update_cost = conversion_float(damages, conversion)
#print(update_cost)
# 2 
# Create a Table
def create_hurricane_dict(names, months, years, max_sustained_winds, areas_affected, deaths, update_cost):
    hurricanes = {}
    for i in range(len(names)):
        hurricane_data = {
            "Name": names[i],
            "Month": months[i],
            "Year": years[i],
            "Max Sustained Wind": max_sustained_winds[i],
            "Areas Affected": areas_affected[i],
            "Deaths": deaths[i],
            "Costs": update_cost[i]
        }
        hurricanes[names[i]] = hurricane_data
    return hurricanes
hurricanes = create_hurricane_dict(names, months, years, max_sustained_winds, areas_affected, deaths, update_cost)
#print(hurricanes)

# 3
# Organizing by Year
def create_hurricane_year_dict(hurricanes):
    hurricanes_year = {}
    for hurricane in hurricanes.values():
        current_year = hurricane["Year"]
        if current_year not in hurricanes_year:
            hurricanes_year[current_year] = []
        hurricanes_year[current_year].append(hurricane)
    return hurricanes_year 
#print(create_hurricane_year_dict(hurricanes))

# 4
# Counting Damaged Areas
def damaged_areas(areas_affected):
  areas = []
  for a in areas_affected:
    for area in a:
      if area not in areas:
        areas.append(area)
  return areas
areas_selected = damaged_areas(areas_affected)
#print(areas_selected)
# create dictionary of areas to store the number of hurricanes involved in
def create_hurricane_affected_dict(areas_selected, hurricanes):
    hurricanes_areas = {}
    for x in range(0, len(areas_selected)):
      number = 0
      for hurricane in hurricanes.values():
        for area in hurricane["Areas Affected"]:
          if area == areas_selected[x]:
            number += 1
      hurricanes_areas[areas_selected[x]] = number
    return hurricanes_areas
times_areas_affected = create_hurricane_affected_dict(areas_selected, hurricanes)
#print(times_areas_affected)
# 5 

# find most frequently affected area and the number of hurricanes involved in
def create_most_frecuent_affected(times_areas_affected):
    area_affected = ''
    num_times = 0
    for key, value in times_areas_affected.items():
      if value > num_times:
        area_affected = key
        num_times = value
    return area_affected
    return num_times
most_frecuent_affected = create_most_frecuent_affected(times_areas_affected)
#print(most_frecuent_affected)
    
# 6

# find highest mortality hurricane and the number of deaths
def create_most_deadliest(hurricanes):
    name = ''
    deaths = 0
    for key, value in hurricanes.items():
      if value["Deaths"] > deaths:
        name = key
        deaths = value["Deaths"]
    return name
    return deaths
deadliest = (create_most_deadliest(hurricanes))
#print(deadliest)
# 7
# Rating Hurricanes by Mortality
def mortality_rating(hurricanes):
  mortality_scale = {0: 0, 1: 100, 2: 500, 3: 1000, 4: 10000}
  mortality_rating = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
  for key, value in hurricanes.items():
    if value["Deaths"] == mortality_scale[0]:
      mortality_rating[0].append(key)
    elif value["Deaths"] > mortality_scale[0] and value["Deaths"] <= mortality_scale[1]:
      mortality_rating[1].append(key)
    elif value["Deaths"] > mortality_scale[1] and value["Deaths"] <= mortality_scale[2]:
      mortality_rating[2].append(key)
    elif value["Deaths"] > mortality_scale[2] and value["Deaths"] <= mortality_scale[3]:
      mortality_rating[3].append(key)
    elif value["Deaths"] > mortality_scale[3] and value["Deaths"] <= mortality_scale[4]:
      mortality_rating[4].append(key)
    else:
      mortality_rating[5].append(key)
  return mortality_rating
mortality_rating = mortality_rating(hurricanes)
#print(mortality_rating)

# 8 Calculating Hurricane Maximum Damage
def highest_cost_hurricane(hurricanes):
    name = ''
    cost = 0
    for key, value in hurricanes.items():
      if value["Costs"] != 'Damages not recorded' and int(value["Costs"]) > cost:
        name = key
        cost = value["Costs"]
    return (name + ' was the most expensive Hurricane with a cost of ' + str(cost) + ' dollars.')
 
# find highest damage inducing hurricane and its total cost
most_expensive_hurricane = highest_cost_hurricane(hurricanes)
#print(most_expensive_hurricane)
# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
  
# categorize hurricanes in new dictionary with damage severity as key
def damage_rating(hurricanes, damage_scale):
  damage_rating = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
  for key, value in hurricanes.items():
    if value["Costs"] == 'Damages not recorded':
      damage_rating[0].append(key)
    elif value["Costs"] > damage_scale[0] and value["Costs"] <= damage_scale[1]:
      damage_rating[1].append(key)
    elif value["Costs"] > damage_scale[1] and value["Costs"] <= damage_scale[2]:
      damage_rating[2].append(key)
    elif value["Costs"] > damage_scale[2] and value["Costs"] <= damage_scale[3]:
      damage_rating[3].append(key)
    elif value["Costs"] > damage_scale[3] and value["Costs"] <= damage_scale[4]:
      damage_rating[4].append(key)
    else:
      damage_rating[5].append(key)
  return damage_rating
damage_rating = damage_rating(hurricanes, damage_scale)
print(damage_rating)