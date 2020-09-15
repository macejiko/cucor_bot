#!/usr/bin/env python3

from abc import ABC, abstractmethod


class Parser(ABC):
    """
    Abstract base class that should be inherited via all parsers

    Possible future parsers:
      - HTMLParser
      - APIParser
    """

    @abstractmethod
    def get_data(self):
        pass

    @abstractmethod
    def get_rates(self):
        pass
