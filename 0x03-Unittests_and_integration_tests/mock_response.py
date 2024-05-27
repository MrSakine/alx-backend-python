#!/usr/bin/env python3
""" Mock response strcuture """
from typing import Dict


class MockResponse:
    """ Mock Response class definition """

    def __init__(self, json_data: Dict, status_code: int = 200):
        """ Data initialization """
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        """ Return json data """
        return self.json_data
