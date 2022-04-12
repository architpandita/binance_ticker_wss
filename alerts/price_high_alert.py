from market_data_wss.factory_market_data import FactoryMarketData
from alerts.print_alert import PrintAlert
from utilities.error_handler import MarketHighAlertError
import yaml
from yaml.loader import SafeLoader
import logging
import json


class PriceHighAlert:
    """
    This is the Alert which will work when the price of the given product get higher or equal to the given value by the user.
    The Class is build such that it should be able to support even new symbols and new exchanges as well.
    We have config file that store the exchange info for websocket.
    """

    user_input = {}

    # default exchange is Binance, this variable is created to provide enough support for future extension
    def __init__(self, config_file=None, exchange="binance"):
        super().__init__()
        # Config have exchange url and port info
        self.file = config_file
        self.exchange = exchange

    @staticmethod
    def read_exchange_config(file):
        # Open the file and load the file
        with open(file) as f:
            data = yaml.load(f, Loader=SafeLoader)
            return data

    @staticmethod
    def fetch_product_and_price(data):
        # this will fetch the price and symbol from the given dictionary
        return float(data.get("p")), data.get("s")

    @staticmethod
    def alert_rule(symbol, price, trigger_price):
        # This is the rule that will decide to raise the alert
        if price >= trigger_price:
            notification = f"The the price for the product {symbol} has crossed trigger price {trigger_price} with CMP: {price}"
            PrintAlert.notify(notification)

    # user_input = {
    #     "symbol": "BTCUSDT",
    #     "trigger_price": 40399
    # }

    @staticmethod
    def alert_scanner(ws, message):
        # this function will be passed to websocket as a on_message for single symbol usecase, so we can run the
        # logic on stream data
        json_msg = json.loads(message)

        logging.info(f"message received {json_msg}")
        price, symbol = PriceHighAlert.fetch_product_and_price(json_msg)
        PriceHighAlert.alert_rule(symbol, price, PriceHighAlert.user_input.get("trigger_price"))

    @staticmethod
    def alert_scanner_for_combine(ws, message):

        # this function will be passed to websocket as a on_message for mutliple symbol usecase, so we can run the
        # logic on stream data

        json_msg = json.loads(message)

        trigger_dict = { v["symbol"]:v["trigger_price"] for v in PriceHighAlert.user_input}
        price, symbol = PriceHighAlert.fetch_product_and_price(json_msg["data"])
        PriceHighAlert.alert_rule(symbol, price, trigger_dict[json_msg["stream"]])

    def start(self, user_input):
        """
        This is the main function for the alert system where all the steps are executed in sequence

        :param user_input:
        :return:
        """
        try:
            PriceHighAlert.user_input = user_input
            logging.info("Alert has started scanning... ")
            param = self.read_exchange_config(self.file)[self.exchange]
            # using logging to log the status
            logging.debug(f"param received {param}")
            # Here we are calling the Binance web socket to fetch the data and process as per alert rule and
            # raise print the data if it matches the cond
            fa = FactoryMarketData()
            binanceObj = fa.get('BinanceMarketDataWSS',**param)
            logging.debug("binanceObj created")

            if isinstance(user_input, dict):
                # if for single symbol
                binanceObj.process_message(PriceHighAlert.alert_scanner)
                binanceObj.connect(user_input["symbol"])

            elif isinstance(user_input, list):
                # for multiple symbol
                binanceObj.process_message(PriceHighAlert.alert_scanner_for_combine)
                build_stream_list = [v["symbol"] for v in user_input]
                binanceObj.combine_stream(build_stream_list)

            logging.debug("binanceObj connection is setup")
            logging.debug("Triggering the run alert ....")
            binanceObj.run()

        except Exception as e:
            raise MarketHighAlertError()
