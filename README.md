# binance_ticker_wss
This is for binance wss and alert on price break out
![image](https://user-images.githubusercontent.com/53426805/162854675-5ed17a72-f1cc-46b2-bc3c-a745a3fa1937.png)




# Main scripts are:
1. user_interactor/start_alert.py : for running the alert or starting point of package
2. market_data_wss/binance_market_data.py : for the websocket interface code to fetch market data
3. alert/price_high_alert.py : for alert rule and checking to raise the alert

# How to use:
Just run this scrip ( user_interactor/start_alert.py ) it will ask for the inputs from the user and then build the input and trigger the function.
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
