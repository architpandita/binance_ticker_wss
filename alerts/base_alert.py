"""
This class is the base class for all the alerts and it will work as a template for all the alerts

"""

class BaseAlert:

    @staticmethod
    def notify(data):
        #  this method will be override based on the the
        raise NotImplementedError(f'Method not implemented')