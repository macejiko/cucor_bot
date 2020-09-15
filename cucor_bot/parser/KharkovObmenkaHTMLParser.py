#!/usr/bin/env python3

from cucor_bot.parser.HTMLParser import HTMLParser


class KharkovObmenkaHTMLParser(HTMLParser):
    def __init__(self):
        self.url = "https://kharkov.obmenka.ua/"
        self.yaml = """
        rate:
            css: li.direction
            xpath: null
            multiple: true
            type: Text
            children:
                currency:
                    css: span.currency
                    xpath: null
                    type: Text
                buy:
                    css: span.buy
                    xpath: null
                    type: Text
                sell:
                    css: span.sell
                    xpath: null
                    type: Text
        """
        super().__init__()

    def get_rates(self):
        for rate in self.data["rate"]:
            currency = rate["currency"].replace(" ", "-").lower()
            buy = rate["buy"].replace(" ", "")
            sell = rate["sell"].replace(" ", "")
            self.rates.append(
                {"currency": currency, "buy": float(buy), "sell": float(sell)}
            )
