#!/usr/bin/env python3

from cucor_bot.currency.Currency import Currency
from cucor_bot.parser.Parser import Parser


class Converter:
    """
    Generator class that does convertion magic

    Requires:
    - Currency that should be converted
    - Parser with available rates dict
    - target_currency list with convertion target. E.g. ['uah','usd']
    """

    def __init__(self, currency, parser, target_currency):
        if isinstance(currency, Currency):
            self.currency = currency
        else:
            raise AttributeError("Incorrect Currency provided!")
        if isinstance(parser, Parser):
            self.parser = parser
        else:
            raise AttributeError("Incorrect Parser provided!")
        self.target_currency = target_currency

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.target_currency) == 0:
            raise StopIteration()

        target = self.target_currency.pop()
        for rate in self.parser.rates:
            if rate["currency"] == "{}-{}".format(self.currency.name, target):
                return Currency(self.currency.amount * rate["buy"], target)
            if rate["currency"] == "{}-{}".format(target, self.currency.name):
                return Currency(self.currency.amount / rate["sell"], target)

        raise RuntimeError("No appropriate currency rate for this values!")
