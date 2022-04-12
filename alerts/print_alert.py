from alerts.base_alert import BaseAlert


class PrintAlert(BaseAlert):
    def __init__(self):
        pass

    @staticmethod
    def notify(data: str):
        print(data)
