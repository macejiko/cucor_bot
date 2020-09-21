#!/usr/bin/env python3

import pytest
from cucor_bot.converter.Converter import Converter
from cucor_bot.currency.Currency import Currency
from cucor_bot.parser.KharkovObmenkaHTMLParser import KharkovObmenkaHTMLParser


class TestConverter:
    @pytest.mark.parametrize(
        "currency, parser, target_currency, result_currency",
        [
            (
                Currency(100, "uah"),
                KharkovObmenkaHTMLParser(),
                ["usd"],
                [Currency(10, "usd")],
            ),
            (
                Currency(150, "rub"),
                KharkovObmenkaHTMLParser(),
                ["uah"],
                [Currency(50, "uah")],
            ),
            (
                Currency(100, "eur"),
                KharkovObmenkaHTMLParser(),
                ["uah"],
                [Currency(500, "uah")],
            ),
            (
                Currency(100, "uah"),
                KharkovObmenkaHTMLParser(),
                ["rub"],
                [Currency(200, "rub")],
            ),
            (
                Currency(100, "eur"),
                KharkovObmenkaHTMLParser(),
                ["usd", "uah"],
                [Currency(150, "usd"), Currency(500, "uah")],
            ),
            (
                Currency(100, "usd"),
                KharkovObmenkaHTMLParser(),
                ["eur", "rub", "gbp"],
                [Currency(50, "eur"), Currency(1600, "rub"), Currency(50, "gbp")],
            ),
        ],
    )
    def test_valid_convertation(
        self, currency, parser, target_currency, result_currency
    ):
        parser.rates = [
            {"currency": "usd-uah", "buy": 8, "sell": 10},
            {"currency": "uah-eur", "buy": 0.1, "sell": 0.2},
            {"currency": "uah-rub", "buy": 2, "sell": 3},
            {"currency": "gbp-uah", "buy": 16, "sell": 20},
            {"currency": "eur-usd", "buy": 1.5, "sell": 2},
            {"currency": "usd-eur", "buy": 0.5, "sell": 1},
            {"currency": "usd-rub", "buy": 16, "sell": 30},
            {"currency": "usd-gbp", "buy": 0.5, "sell": 2},
        ]
        for c in Converter(currency, parser, target_currency):
            r = result_currency.pop()
            assert c.name == r.name
            assert c.amount == r.amount
