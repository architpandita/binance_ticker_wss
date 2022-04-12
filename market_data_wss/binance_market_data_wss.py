from market_data_wss.base_market_data_wss import MarketDataWSS
import websocket


class BinanceMarketDataWSS(MarketDataWSS):
    """
    This is the class which interact with the binance web socket and fetch the data based on symbol

    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ws = None
        self.msg_fxn = None

    @staticmethod
    def _on_close(ws):
        print("Socket is closed now")

    @staticmethod
    def _on_message(ws, message):
        print(f"---- {message}")

    @staticmethod
    def _on_error(ws):
        print("ERROR occured!")

    def process_message(self, fxn=None):
        if fxn:
            self.msg_fxn = fxn
        else:
            self.msg_fxn = BinanceMarketDataWSS._on_message

    #/ stream?streams = < streamName1 > / < streamName2 > /
    def combine_stream(self, symbol_list):
        """
        To support combine stream we have differ way to call the websocket url using streams

        :param symbol_list:
        :return:
        """
        socket = self.wss_url + ":" + str(self.wss_port)
        comb_list = "/".join(symbol_list)

        stream_url = f"/stream?streams={comb_list}"

        full_socket = socket + stream_url
        self.ws = websocket.WebSocketApp(full_socket, on_close=BinanceMarketDataWSS._on_close,
                                         on_message=self.msg_fxn,
                                         on_error=BinanceMarketDataWSS._on_error)

    def connect(self, symbol):
        """
                To support combine stream we have differ way to call the websocket url using ws

                :param symbol:
                :return:
                """
        socket = self.wss_url + ":" + str(self.wss_port)
        stream_url = f"/ws/{symbol}"

        full_socket = socket+stream_url
        self.ws = websocket.WebSocketApp(full_socket, on_close=BinanceMarketDataWSS._on_close,
                                         on_message=self.msg_fxn,
                                         on_error=BinanceMarketDataWSS._on_error)

    def run(self):
        """
        This will run the websocket continously
        :return:
        """
        self.ws.run_forever()

    def stop(self):
        """
        We can use this function to stop the websoket
        :return:
        """
        self.ws.keep_running = False


