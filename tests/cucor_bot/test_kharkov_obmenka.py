#!/usr/bin/env python3

import pytest
import re
from cucor_bot.parser.KharkovObmenkaHTMLParser import KharkovObmenkaHTMLParser


class TestKharkovObmenkaHTMLParser:
    def test_get_data(self):
        parser = KharkovObmenkaHTMLParser()
        parser.get_data()
        assert isinstance(parser.data, dict)
        assert len(parser.data["rate"]) != 0
        assert len(parser.data["rate"][0]["currency"]) != 0
        assert len(parser.data["rate"][0]["buy"]) != 0
        assert len(parser.data["rate"][0]["sell"]) != 0

    def test_get_rates(self):
        parser = KharkovObmenkaHTMLParser()
        parser.get_data()
        parser.get_rates()
        assert isinstance(parser.rates, list)
        assert len(parser.rates) != 0
        assert re.search("[a-z]{3}-[a-z]{3}", parser.rates[0]["currency"])
        assert parser.rates[0]["buy"] > 0
        assert parser.rates[0]["sell"] > 0
