from alerts.base_alert import BaseAlert
from alerts.print_alert import PrintAlert
from alerts.price_high_alert import PriceHighAlert


class FactoryAlert:
    """
    This is the Factory class that is used to create the object for given class on the runtime.

    """
    def __init__(self):
        # list of all the classed assigned
        self.all_classes = globals()

    # below method will return the object of the class needed
    def get(self,name,config_path, exchange):
        return self.all_classes[name](config_path, exchange)
