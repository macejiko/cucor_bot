#!/usr/bin/env python3

import re


class Currency:
    """
    This class presents any coin in the system
    """

    def __init__(self, amount=0, name="uah"):
        """
        Valid amount int or float
        Valid name with 3 chars. E.g. 'usd', 'uah', 'rub'
        """
        if (
            len(name) != 3
            or not isinstance(amount, float)
            and not isinstance(amount, int)
        ):
            raise AttributeError("Incorrect amount or name provided!")
        self.amount = amount
        self.name = name

    def get_from_string(self, string):
        """
        Available string values. Amount should be int:

            Currency('7uah')
            Currency('5 usd')

        All another values will raise AttributeError
        """

        res = re.search("[a-zA-Z]+$", string)
        if res:
            self.name = res.group(0)
        else:
            raise (AttributeError("Cannot find currency name! Input example: '15usd'"))

        res = re.search("^[0-9]+", string)
        if res:
            self.amount = int(res.group(0))
        else:
            raise (
                AttributeError("Cannot find currency amount! Input example: '15usd'")
            )
