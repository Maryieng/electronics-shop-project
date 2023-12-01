import unittest

import pytest

from src.item import Item


@pytest.fixture
def item():
    return Item("Смартфон", 10000, 20)


def test_calculate_total_price(item):
    assert item.calculate_total_price() == 200000


def test_apply_discount(item):
    item.apply_discount()
    assert item.price == 0.0


def test_name(item):
    item.name = "Смартфон"
    assert item.name == "Смартфон"
    item.name = "СуперСмартфон"
    assert item.name == "СуперСмарт"
    item.name = "Супер"
    assert item.name == "Супер"


class ItemTestCase(unittest.TestCase):
    def setUp(self):
        self.sample_csv = 'sample.csv'

    def tearDown(self):
        Item.all = []

    def test_instantiate_from_csv(self):
        with open(self.sample_csv, 'w') as f:
            f.write("name,price,quantity\n")
            f.write("Item 1,10.99,5\n")
            f.write("Item 2,5.99,3\n")

        Item.instantiate_from_csv(self.sample_csv)
        self.assertEqual(len(Item.all), 2)
        self.assertEqual(Item.all[0].name, "Item 1")
        self.assertEqual(Item.all[0].price, 10)
        self.assertEqual(Item.all[0].quantity, 5)
        self.assertEqual(Item.all[1].name, "Item 2")
        self.assertEqual(Item.all[1].price, 5)
        self.assertEqual(Item.all[1].quantity, 3)

    def test_nonexistent_csv(self):
        nonexistent_csv = 'sample.csv'
        Item.instantiate_from_csv(nonexistent_csv)

    def test_string_conversion(self):
        with open(self.sample_csv, 'w') as f:
            f.write("name,price,quantity\n")
            f.write("Item 1,5,3\n")

        Item.instantiate_from_csv(self.sample_csv)
        self.assertEqual(Item.all[0].price, 5)
        self.assertEqual(Item.all[0].quantity, 3)
        self.assertIsInstance(Item.all[0].price, int)
        self.assertIsInstance(Item.all[0].quantity, int)


    def test_repr_str(self):
        item1 = Item("Смартфон", 10000, 20)
        assert repr(item1) == "Item('Смартфон', 10000, 20)"
        assert str(item1) == 'Смартфон'

        item1 = Item("Камера", 100000, 50)
        assert repr(item1) == "Item('Камера', 100000, 50)"
        assert str(item1) == 'Камера'


