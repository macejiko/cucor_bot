#!/usr/bin/env python3

import pytest
from cucor_bot.currency.Currency import Currency


class TestCurrency:
    @pytest.mark.parametrize(
        "input_amount, input_name, result_amount, result_name",
        [(100, "rub", 100, "rub"), (9.99, "eur", 9.99, "eur")],
    )
    def test_constructor_valid(
        self, input_amount, input_name, result_amount, result_name
    ):
        c = Currency(input_amount, input_name)

        assert c.amount == result_amount
        assert c.name == result_name

    @pytest.mark.parametrize(
        "input_amount, input_name",
        [
            ("3", "eur"),
            ("5.55", "usd"),
            ("aaa", "uah"),
            (10, "us"),
            (5, "@#$"),
            (7, "rubb"),
            (9, "aaa"),
            (4, "bb"),
            (6, ""),
            ("", ""),
            ("", "usd"),
            (None, None),
        ],
    )
    def test_constructor_invalid(self, input_amount, input_name):
        with pytest.raises(AttributeError):
            assert Currency(input_amount, input_name)

    @pytest.mark.parametrize(
        "valid, name, amount",
        [
            ("15usd", "usd", 15),
            ("7 uah", "uah", 7),
            ("888.88 rub", "rub", 888.88),
            ("77.7eur", "eur", 77.7),
        ],
    )
    def test_valid_string(self, valid, name, amount):
        c = Currency()
        c.get_from_string(valid)

        assert c.name == name
        assert c.amount == amount

    @pytest.mark.parametrize(
        "invalid",
        [
            "usd",
            "8lol",
            "3.33hah",
            "3ua",
            "8.9ru",
            "uah7",
            "eur3.14",
            "eur 10",
            "rub 2.66",
            "ru 2.66",
            "eu 2",
            "us55",
            "gb5.5",
            "AAA",
            "777",
            "None",
            "!#?$",
            "5$",
            "http://pythong.org",
            True,
        ],
    )
    def test_invalid_string(self, invalid):
        c = Currency()
        with pytest.raises(AttributeError):
            assert c.get_from_string(invalid)
