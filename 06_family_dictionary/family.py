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

print({relation:{key:value for (key,value) in stats.items()} for (relation, stats) in my_family.items()})