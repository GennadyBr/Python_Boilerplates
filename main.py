""" FastAPI Boilerplate Library """
import logging
import os
import sys
from typing import List

logger = logging.getLogger(__name__)


def print_hello(user_name: str = 'DEFAULT', list_a: List | None = None) -> str:
    """
    :param user_name: str
    :param list_a: List
    :return: str
    """
    abc: List = sys.path
    bcd: str = str(os.path)

    return f'Hello, {user_name}///// {list_a}///// {abc}///// {bcd}'


def append_to_list(value: int, my_list: List | None = None) -> List:
    """
    :param value: int
    :param my_list: List
    :return: List
    """
    if my_list is None:
        my_list = []
    new_value = [
        2,
        3,
        value,
    ]
    my_list.append(new_value)
    return my_list


if __name__ == '__main__':
    name: str = input("What's your name? ")
    logger.info(print_hello(name))

    result1 = append_to_list(1)
    logger.info(result1)  # Вывод: [1]

    result2 = append_to_list(2)
    logger.info(result2)  # Вывод: [1, 2]
