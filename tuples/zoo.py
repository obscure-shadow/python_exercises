# Create a tuple named `zoo` that contains your favorite animals.
zoo = 'cat', 'armadillo', 'sloth', 'anteater'
# Find one of your animals using the `.index(value)` method on the tuple.
print(zoo[2])
# Determine if an animal is in your tuple by using `for value in tuple`.
for v in zoo:
    if v == 'sloth':
        print("there's a sloth")
# Create a variable for each of the animals in your tuple with this cool feature of Python.

#     ```
#     # example
#     (lizard, fox, mammoth) = zoo
#     print(lizard)
#     ```
(cat, armadillo, sloth, anteater) = zoo
print(armadillo)
# 1. Convert your tuple into a list.
zoo_list= list(zoo)
print(zoo_list)
# 1. Use `extend()` to add three more animals to your zoo.
zoo_list.extend(['lemur', 'panda', 'echidna'])
print(zoo_list)
# 1. Convert the list back into a tuple.
zoo = tuple(zoo_list)