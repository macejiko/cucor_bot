#!/usr/bin/env python3

import pytest
from cucor_bot.currency.Currency import Currency


class TestCurrency:
    @pytest.mark.parametrize(
        "invalid",
        [
            "usd",
            "8lol",
            "uah7",
            "AAA",
            "777",
            "None",
            "eur 10",
            "!#?$",
            "5$",
            "3ua",
            "http://pythong.org",
        ],
    )
    def test_invalid_creation(self, invalid):
        with pytest.raises(AttributeError):
            assert Currency(invalid)

    @pytest.mark.parametrize(
        "valid,name,amount", [("15usd", "usd", 15), ("7 uah", "uah", 7)]
    )
    def test_valid_creation(self, valid, name, amount):
        cur = Currency(valid)

        assert cur.name == name
        assert cur.amount == amount
