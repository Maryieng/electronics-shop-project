from src.phone import Phone


def test_number_of_sim_getter():
    phone = Phone("iPhone 14", 120_000, 5, 2)
    phone.number_of_sim = 3
    assert phone.number_of_sim == 3


def test_number_of_sim_setter():
    phone = Phone("iPhone 14", 120_000, 5, 2)
    try:
        phone.number_of_sim = -1
        assert False, "Expected a ValueError to be raised"
    except ValueError as e:
        assert str(e) == 'Количество физических SIM-карт должно быть целым числом больше нуля.'
