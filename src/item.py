import csv
import math
import os
from typing import Any


class InstantiateCSVError(Exception):
    """ Обработка исключений при повреждении файла """
    def __init__(self, message) -> None:
        """ Инициализация экземпляра класса """
        self.message = message

    def __str__(self) -> str:
        """ Вывод информации для пользователя: текст ошибки """
        return f'{self.message}'


class Item:
    """Класс для представления товара в магазине. """
    pay_rate = 1.0
    all = []   # type: ignore

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """ Создание экземпляра класса item."""
        self.__name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self) -> str:
        """ отображение информации об объекте класса в режиме отладки """
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self) -> str:
        """ отбражение информации об объекте класса для пользователей """
        return f"{self.__name}"

    def __add__(self, other) -> Any:
        """ Сложение товаров """
        if isinstance(other, Item):
            return int(self.quantity) + int(other.quantity)
        raise ValueError('Складывать можно только объекты Item и дочерние от них.')

    @property
    def name(self) -> str:
        """ Возвращает наименование товара. """
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        """ Устанавливает наименование товара. """
        if len(name) > 10:
            self.__name = name[:10]
        else:
            self.__name = name

    def calculate_total_price(self) -> float:
        """ Рассчитывает общую стоимость конкретного товара в магазине."""
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """ Применяет установленную скидку для конкретного товара. """
        self.price = self.price - self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls, filename: str) -> None:
        """инициализирует экземпляры класса Item данными из файла src/items.csv"""
        cls.all.clear()
        path_filename = os.path.join(os.path.dirname(__file__), filename)
        try:
            with open(path_filename, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for line in reader:
                    if 'name' not in line or 'price' not in line or 'quantity' not in line:
                        raise InstantiateCSVError('Файл item.csv поврежден')
                    name = line['name']
                    price = Item.string_to_number(line['price'])
                    quantity = int(line['quantity'])
                    item = cls(name, price, quantity)
                    Item.all.append(item)
        except FileNotFoundError:
            raise FileNotFoundError('Отсутствует файл items.csv')

    @staticmethod
    def string_to_number(string: str) -> float:
        """Преобразование строки в число"""
        return int(math.floor(float((string.replace(',', '.')))))
