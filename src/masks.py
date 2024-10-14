
from typing import Union

card_number_str = int()
account_str = int()


def get_mask_card_number(card_number: Union[str]) -> Union[str]:
    """Функция принимает на вход номер карты и возвращает ее маску"""
    if len(card_number) == 16 and card_number.isdigit() == True:
        return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    return "Некорректный ввод"


def get_mask_account(account_number: str) -> str:
    """Функция принимает на вход номер счета и возвращает ее маску"""
    if len(account_number) == 20 and account_number.isdigit() == True:
        return f"{account_number[-4:]}"
    return "Некорректный ввод"
