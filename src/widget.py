from typing import Union

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(type_card_num: str) -> str:
    """Функция, для выводв номера карты или счета с текстом"""
    type_card_num_list = type_card_num.split(" ")
    if len(type_card_num_list[-1]) < 20 and len(type_card_num) > 16:
        mask_card_number = get_mask_card_number(type_card_num_list[-1])
        type_card_num_list[-1] = mask_card_number
        if mask_card_number == "Некорректный ввод":
            return "Некорректный ввод данных"
        return " ".join(type_card_num_list)
    if len(type_card_num_list[-1]) == 20 and len(type_card_num) == 25:
        mask_account = get_mask_account(type_card_num_list[-1])
        type_card_num_list[-1] = mask_account
        return " ".join(type_card_num_list)
    return "Некорректный ввод данных"


def get_date(date: Union[str]) -> Union[str] | None:
    """Функция преобразовывает дату в формате 'ДД.ММ.ГГГГ'"""
    if type(date) != str:
        return "Неверный тип данных"
    if len(date) == 26 and date[4] == "-" and date[7] == "-" and date[-7] == ".":
        return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"
    return "Некорректное значение даты"
