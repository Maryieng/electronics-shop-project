import unittest

import pytest

from src.item import InstantiateCSVError, Item
from src.phone import Phone


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

    def test_repr_str(self):
        item1 = Item("Смартфон", 10000, 20)
        assert repr(item1) == "Item('Смартфон', 10000, 20)"
        assert str(item1) == 'Смартфон'

        item1 = Item("Камера", 100000, 50)
        assert repr(item1) == "Item('Камера', 100000, 50)"
        assert str(item1) == 'Камера'

    def test_add(self):
        phone1 = Phone("iPhone 14", 120_000, 5, 2)
        item1 = Item("Камера", 100000, 50)
        assert item1.quantity + phone1.quantity == 55
        assert item1.quantity + item1.quantity == 100
        assert phone1.quantity + phone1.quantity == 10

    def test_instantiate_from_csv(self):
        Item.instantiate_from_csv("items.csv")
        self.assertEqual(len(Item.all), 5)

    def test_instantiate_from_csv_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            Item.instantiate_from_csv("nonexistent.csv")

    def test_instantiate_from_csv_corrupted_file(self):
        with self.assertRaises(InstantiateCSVError):
            Item.instantiate_from_csv("corrupted.csv")
