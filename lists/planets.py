planet_list = ["Mercury", "Mars"]
planet_list.append('Jupiter')
planet_list.append('Saturn')
print(planet_list)
real_planets = ['Neptune', 'Pluto']
planet_list.extend(real_planets)
print(planet_list)
planet_list.append('Pluto')
print(planet_list)
rocky_planets = planet_list[:2]
print(rocky_planets)
del(planet_list[6])
print(planet_list)
