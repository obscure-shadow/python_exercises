my_family = {
    'sister': {
        'name': 'Krista',
        'age': 42
    },
    'mother': {
        'name': 'Cathie',
        'age': 70
    },
    'brother': {
        'name': 'neil',
        'age': 20
    }
}

for rln, val in my_family.items():
    for stat, value in val.items():
        print(f"my {rln}'s {stat} is {value}\n")


print({ "my " + relation + "s" :{ key + " is":value for (key,value) in stats.items()}
    for (relation, stats) in my_family.items()})

