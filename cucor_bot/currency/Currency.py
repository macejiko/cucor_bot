#!/usr/bin/env python3

import re


class Currency:
    def __init__(self, string):
        """
        Available string values:

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
