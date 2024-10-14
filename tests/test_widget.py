import pytest

from src.widget import get_date, mask_account_card

@pytest.mark.parametrize(
    "value, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет 4305"),
    ],
)
def test_mask_account_card_basic(value: str, expected: str) -> None:
    """Тест на срабатыание функции с корректным номером карты и счета"""
    assert mask_account_card(value) == expected


@pytest.mark.parametrize(
    "value, expected",
    [
        ("7000792289606361", "Некорректный ввод данных"),
        ("Счет", "Некорректный ввод данных"),
        ("Maestro 7000792289606361", "Maestro 7000 79** **** 6361"),
        ("MasterCard 7000792289606361", "MasterCard 7000 79** **** 6361"),
        ("Visa Classic 7000792289606361", "Visa Classic 7000 79** **** 6361"),
        ("MasterCard 7000792289606361", "MasterCard 7000 79** **** 6361"),
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Visa Gold 7000792289606361", "Visa Gold 7000 79** **** 6361"),
        ("Visa Gold 700079228960636", "Некорректный ввод данных"),
    ],
)
def test_mask_account_card_various_input_data(value: str, expected: str) -> None:
    assert mask_account_card(value) == expected


"""Тесты для get_date"""


def test_get_date_basic() -> None:
    """Срабатывание с данными '2018-10-14T08:21:33.419441'"""
    assert get_date("2018-10-14T08:21:33.419441") == "14.10.2018"


@pytest.mark.parametrize(
    "value, expected",
    [
        ("08:21:33.419441", "Некорректное значение даты"),
        ("2018-14T08:21:33.419441", "Некорректное значение даты"),
    ],
)
def test_get_date_uncorrectly_date(value: str, expected: str) -> None:
    """Срабатывание функции с некорректным значением даты"""
    assert get_date(value) == expected