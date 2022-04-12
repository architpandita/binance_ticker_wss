from unittest import TestCase
from market_data_wss.binance_market_data_wss import BinanceMarketDataWSS


class TestBinanceMarketDataWSS(TestCase):

    def setUp(self) -> None:
        """
        Initializing the param
        :return:
        """
        inp = {
            "url": "xyz",
               "port":1111
               }
        self.obj = BinanceMarketDataWSS(**inp)

    def tearDown(self) -> None:
        pass

    def test_process_message(self):
        f = lambda x:x+1
        self.assertTrue(self.obj.process_message(f), f)