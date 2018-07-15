import unittest
import sys
sys.path.append('../')
from animals import Animal
from animals import Dog

class TestAnimal(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.bob = Dog("Bob")

    def test_animal_creation(self):

        bob = Dog("Bob")

        self.assertIsInstance(bob, Dog)
        self.assertIsInstance(bob, Animal)

    def test_animals_can_set_legs(self):
        self.bob.set_legs(6)
        self.assertEqual(self.bob.legs, 6)

if __name__=='__main__':
    unittest.main()