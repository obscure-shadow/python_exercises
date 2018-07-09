from animal import Animal

class Dog(Animal):
    def __init__(self, breed):
        self.breed = breed
        super().__init__('dog', leg_num=4, domesticated=True)

    def speak(self):
            return f'I am a dog, and i like to say {self.say_something()}'