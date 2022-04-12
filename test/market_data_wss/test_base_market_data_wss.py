from unittest import TestCase
import unittest
from market_data_wss.base_market_data_wss import MarketDataWSS

class TestMarketDataWSS(TestCase):

    def setUp(self) -> None:
        inp = {
            "url": "xyz",
               "port":1111
               }
        self.obj = MarketDataWSS(**inp)


    def tearDown(self) -> None:
        pass

    def test_connect(self):
        with self.assertRaises(NotImplementedError):
            self.obj.connect("xyz")

