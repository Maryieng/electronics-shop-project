from typing import Any

from src.item import Item


class Phone(Item):
    """ Класс для телефонов как товаров """
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        """ Создание экземпляра класса Phone."""
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __repr__(self) -> str:
        """ отображение информации об объекте класса в режиме отладки """
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    @property
    def number_of_sim(self) -> int:
        """ отображение информации о количестве сим-карт """
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number_sim: int) -> Any:
        """ Проверка количества сим-карт """
        if number_sim <= 0:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')
        else:
            self.__number_of_sim = number_sim
