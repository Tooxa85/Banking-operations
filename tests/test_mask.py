import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number_basic() -> None:
    """Тест на срабатывание функции при введении номера карты"""
    assert get_mask_card_number("4276060032300678") == "4276 06** **** 0678"


"""Параметризация функции get_mask_card_number"""


@pytest.mark.parametrize(
    "value, expected",
    [
        ("4276060032300678000000000", "Некорректный ввод"),
        ("zhyenkfudjlpdoiu", "Некорректный ввод"),
        ("1l4.dlg8pr-a8]6m", "Некорректный ввод"),
        ("4276060032300", "Некорректный ввод"),
        ("", "Некорректный ввод"),
    ],
)
def test_get_mask_card_number_various_input_data(value, expected) -> None:
    """Тест на срабатывание функции при введении различных некоректных данных"""
    assert get_mask_card_number(value) == expected


def test_get_mask_account_basic() -> None:
    """Тест на срабатывание функции при введении номера счета"""
    assert get_mask_account("12345678901234567890") == "7890"


"""Параметризация функции get_mask_account"""


@pytest.mark.parametrize(
    "value, expected",
    [
        ("1234567890123456789012365", "Некорректный ввод"),
        ("p2o6jdmb80djeyabd,97", "Некорректный ввод"),
        ("dfngjdfgdf;gjkdgjief", "Некорректный ввод"),
        ("12345678901234567", "Некорректный ввод"),
        ("", "Некорректный ввод"),
    ],
)
def test_get_mask_account_various_input_data(value, expected) -> None:
    """Тест на срабатывание функции при введении различных некоректных данных"""
    assert get_mask_account(value) == expected