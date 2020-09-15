#!/usr/bin/env python3

from cucor_bot.parser.Parser import Parser
from selectorlib import Extractor
import requests


class HTMLParser(Parser):
    """
    Base class for getting data from url via selectorlib
    Gets html data via requests and parses result data via provided yml string
    """

    def __init__(self):
        self.data = {}
        self.rates = []

    def get_data(self):
        e = Extractor.from_yaml_string(self.yaml)
        r = requests.get(self.url)
        self.data = e.extract(r.text)
