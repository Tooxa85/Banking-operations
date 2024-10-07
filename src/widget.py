from typing import Union

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(nums: Union[str]) -> Union[str] | None:
    """Функция маскировки карты и счета"""
    if "Счет" in nums:
        return "Счет " + get_mask_account(nums)
    else:
        cards = get_mask_card_number(nums[-16:])
        new_card = nums.replace(nums[-16:], cards)
        return new_card


def get_date(date: Union[str]) -> Union[str] | None:
    """Функция преобразовывает дату в формате 'ДД.ММ.ГГГГ'"""
    return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"
