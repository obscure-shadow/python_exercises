showroom = set([ 'nissan leaf', 'toyota prius', 'honda insight gen1', 'e type jaguar'])
print("lenght of showroom " + str(len(showroom)) )
showroom.add('nissan leaf')
print(f'does this work?{showroom}')
showroom.update(['lancia scorpion', 'porsche 911'])
print(f'updated with lancia scorpion and porshe {showroom}')
showroom.discard('porsche 911')
print(f'discarded porcshe: {showroom}')
junkyard = set([ 'toyota carolla', 'lancia scorpion', 'vw rabbit', 'toyota prius'])
print(f'added junkyard cars : {junkyard}')
print(f'intersection of junkyard and showroom {junkyard.intersection(showroom)}')
print(f'junkyard and showroom union: {junkyard.union(showroom)}')
new_showroom = junkyard.union(showroom)
new_showroom.discard("toyota carolla")
new_showroom.discard("vw rabbit")
print(f'new showroom minus bs stuff {new_showroom}')
