#!/usr/bin/env python3

import pytest
from cucor_bot.converter.Converter import Converter
from cucor_bot.currency.Currency import Currency
from cucor_bot.parser.KharkovObmenkaHTMLParser import KharkovObmenkaHTMLParser


class TestConverter:
    def setup_method(self):
        self.parser = KharkovObmenkaHTMLParser()
        self.parser.rates = [
            {"currency": "usd-uah", "buy": 8, "sell": 10},
            {"currency": "uah-eur", "buy": 0.1, "sell": 0.2},
            {"currency": "uah-rub", "buy": 2, "sell": 3},
            {"currency": "gbp-uah", "buy": 16, "sell": 20},
            {"currency": "eur-usd", "buy": 1.5, "sell": 2},
            {"currency": "usd-eur", "buy": 0.5, "sell": 1},
            {"currency": "usd-rub", "buy": 16, "sell": 30},
            {"currency": "usd-gbp", "buy": 0.5, "sell": 2},
        ]

    @pytest.mark.parametrize(
        "currency, target_currency, result_currency",
        [
            (
                Currency(100, "uah"),
                ["usd"],
                [Currency(10, "usd")],
            ),
            (
                Currency(150, "rub"),
                ["uah"],
                [Currency(50, "uah")],
            ),
            (
                Currency(100, "eur"),
                ["uah"],
                [Currency(500, "uah")],
            ),
            (
                Currency(100, "uah"),
                ["rub"],
                [Currency(200, "rub")],
            ),
            (
                Currency(100, "eur"),
                ["usd", "uah"],
                [Currency(150, "usd"), Currency(500, "uah")],
            ),
            (
                Currency(100, "usd"),
                ["eur", "rub", "gbp"],
                [Currency(50, "eur"), Currency(1600, "rub"), Currency(50, "gbp")],
            ),
        ],
    )
    def test_valid_convertation(self, currency, target_currency, result_currency):
        for c in Converter(currency, self.parser, target_currency):
            r = result_currency.pop()
            assert c.name == r.name
            assert c.amount == r.amount

    def test_invalid_currency(self):
        with pytest.raises(AttributeError):
            assert Converter(None, self.parser, ["usd"])

    def test_invalid_parser(self):
        with pytest.raises(AttributeError):
            assert Converter(Currency(100, "uah"), None, ["usd"])

    @pytest.mark.parametrize(
        "target_currency",
        [
            None,
            ["inv"],
            [None],
            ["inv", "usd"],
            ["@@@@", "usd"],
            [],
            [""],
            ["uah"],
        ],
    )
    def test_invalid_target_currency(self, target_currency):
        with pytest.raises(AttributeError):
            Converter(Currency(100, "uah"), self.parser, target_currency)
