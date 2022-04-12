from utilities.error_handler import UserInputError
from alerts.factory_alert import FactoryAlert
from utilities.error_handler import StartAlertError
import logging


"""
This script will help the user to pass and run in the values and symbols required to run the alert system.
It used Factory to create different alerts based on the request made by the user. 

"""


def _validate_user_input(user_input: dict) -> None:
    if user_input.get("trigger_price") < 0:
        raise UserInputError


def _validate_user_input_combine(user_input: list) -> None:
    for v in user_input:
        if v.get("trigger_price") < 0:
            raise UserInputError


def start_alert(user_input: dict) -> None:
    # validate_user_input(user_input)

    exchange = "binance"
    config_path = "resource/exchange_config.yml"
    fa = FactoryAlert()
    alert_obj = fa.get('PriceHighAlert', config_path, exchange)
    alert_obj.start(user_input)


def start_alert_multiple(user_input: list) -> None:
    # validate_user_input(user_input)
    exchange = "binance"
    config_path = "resource/exchange_config.yml"
    fa = FactoryAlert()
    alert_obj = fa.get('PriceHighAlert', config_path, exchange)
    alert_obj.start(user_input)


def _make_user_input_single() -> dict:
    _user_input = {}
    sym = input("Please enter the symbol eg: sym@trade \n")
    t_price = float(input("Please enter the trigger price for Alert for high \n"))
    _user_input["symbol"] = sym
    _user_input["trigger_price"] = float(t_price)
    return _user_input


def _make_user_input_multiple() -> list:
    list_user_input = []
    pro_count = input("Please enter total no. of products you want to track \n")

    for i in range(int(pro_count)):
        _user_input = dict()
        sym = input("Please enter the symbol eg: sym@trade  \n")
        t_price = float(input("Please enter the trigger price for Alert for high \n"))
        _user_input["symbol"] = sym
        _user_input["trigger_price"] = float(t_price)
        list_user_input.append(_user_input)
    return list_user_input


if __name__ == "__main__":
    """
    Just run this scrip it will ask for the inputs from the user and then build the input and trigger the function.
    We will support both single and multiple symbol alert
    
    Note: 
    We can use a web page using socket or jquery to do the same thing but this is build to keep the solution simple.
    
    For Test:
    Input:
        Please enter 1 for Single product and 2 for multiple product 
        1
        Please enter the symbol eg: sym@trade 
        btcusdt@trade
        Please enter the trigger price for Alert for high 
        30000
    
    output: 
        The the price for the product BTCUSDT has crossed trigger price 30000.0 with CMP: 39468.79
    """
    try:
        logging.info("the process of alert is starting...")
        # this is to ask for what type user is looking for
        val = input("Please enter 1 for Single product and 2 for multiple product \n")
        logging.debug(f"user have selected opt {val}")
        user_input = dict()
        # user_input = {
        #          "symbol": "bnbusdt@trade",
        #          "trigger_price": 380
        #      }

        # ## for multiple symbol
        # user_input = [{
        #     "symbol": "bnbusdt@trade",
        #     "trigger_price": 380
        # },
        #     {
        #         "symbol": "btcusdt@trade",
        #         "trigger_price": 39019
        #     }]

        if val == '1':
            # run alert for the single symbol
            logging.debug("running code for single symbol")
            start_alert(_make_user_input_single())
        elif val == '2':
            # run alert for multiple symbols
            logging.debug("running code for multiple symbol")
            start_alert_multiple(_make_user_input_multiple())
    except Exception as e:
        raise StartAlertError()


