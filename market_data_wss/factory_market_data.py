from market_data_wss.binance_market_data_wss import BinanceMarketDataWSS


class FactoryMarketData:
    """
    This is the Factory class that is used to create the object for given class on the runtime.

    """
    def __init__(self):
        # list of all the classed assigned
        self.all_classes = globals()

    # below method will return the object of the class needed
    def get(self,name,**kwargs):
        return self.all_classes[name](**kwargs)
