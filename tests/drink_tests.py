import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("Tennents", 5.00, 4)

    def test_drink_has_name(self):
        self.assertEqual("Tennents", self.drink.name)

    def test_drink_has_price(self):
        self.assertEqual(5.00, self.drink.price)

    def test_drink_has_alcohol_level(self):
        self.assertEqual(4, self.drink.alcohol_level)