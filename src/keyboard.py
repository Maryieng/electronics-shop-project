from src.item import Item


class MixinLanguage:
    """ Миксин-класс для хранения и изменения раскладки клавиатуры """
    def __init__(self):
        """ Инициализация миксина"""
        self.__language = 'EN'

    @property
    def language(self):
        """ Режим доступа для языка клавиатуры """
        return self.__language

    def change_lang(self):
        """ Изменение языка """
        if self.__language == 'EN':
            self.__language = 'RU'
        else:
            self.__language = 'EN'
        return self


class Keyboard(Item, MixinLanguage):
    """ Класс для товара клавиатура """
    def __init__(self, name: str, price: float, quantity: int) -> None:
        """ Создание экземпляра класса Keyboard."""
        super().__init__(name, price, quantity)
        MixinLanguage.__init__(self)
