from animal import Animal

class Pet(Animal, Species):
    def __init__(self, name, species):
        self.name = name
        self.animal_type = species

    def set_owner(self, name, phone):
        self.owner_name = name
        self.owner_number = phone

    def __str__(self):
        return f'This pet\'s name is {slef.name}. It has {self.animal_type.leg_num_} legs
        and likes to say {self.animal_type.saySomething()}!'


