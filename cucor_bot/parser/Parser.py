#!/usr/bin/env python3

from abc import ABC, abstractmethod


class Parser(ABC):
    @abstractmethod
    def get_data(self):
        pass

    @abstractmethod
    def get_rates(self):
        pass
