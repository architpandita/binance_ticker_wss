class MarketDataWSS:
    """
    This base class will work as template for all the other classes of Marketdata for differ Exchanges
    """
    def __init__(self, **kwargs):
        self.wss_url = kwargs.get("url")
        self.wss_port = kwargs.get("port")

    def connect(self, symbol):
        raise NotImplementedError(f'Method not implemented for {type(self).__name__}.')
