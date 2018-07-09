def looper(list, num, str='foo'):
    for item in list[:num]:
        if str == "I have viseted the city of" and item == "Kansas City":
            print(f"{str} {item}")

cities = ['Kansas City', 'Wichata', 'Omaha', 'Nashville']

looper(cities, 3, 'I have viseted the city of')
