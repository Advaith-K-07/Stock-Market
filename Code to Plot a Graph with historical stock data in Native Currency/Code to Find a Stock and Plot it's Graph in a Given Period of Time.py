import yfinance as yf #Yahoo Finance Library to Access Stock Information.
import pandas as pd
import matplotlib.pyplot as plt 
import requests    #To access the ticker while providing Stock's Original Name.


#NOTE :- This code tries to retrieve the stock's information in NATIVE CURRENCY.
#Currently supports Japan, India (NSE and BSE), Singapore, Hong Kong, London.


def get_ticker(company_name):
    url = f"https://query2.finance.yahoo.com/v1/finance/search?q={company_name}" #Searches the Companies' Tricker and Gives it to us.
    headers = {"User-Agent": "Chrome/6.0"}
    response = requests.get(url, headers=headers)
    data = response.json()
    preferred_suffixes = [".T", ".NS", ".BO", ".SI", ".HK", ".L", ""]  # (To get native currency).

    if data.get("quotes"):
        quotes = data["quotes"]
        for suffix in preferred_suffixes:
            for quote in quotes:
                symbol = quote.get("symbol", "")
                if symbol.endswith(suffix):
                    return symbol  #Return native ticker.





    #Returning the Value of the tricker so that we can use it further in the code.







stock_name = str(input("Enter the name of the stock :- "))  #Simplifying the User's Job in just entering the stock's name.

ticker = get_ticker(stock_name)
stock = yf.Ticker(ticker) #Gives the stock info, like currency, sector, name, etc.
info = stock.info #Gives Stock info like Hinstorial data, max high, max low, etc.

fast_info = stock.fast_info #Accessing the currency in which the stock trades in.

loc_currency = fast_info.get("currency", info.get("currency", "Unknown"))
                                    #NOTE :- USE FORMAT FOR TIME :- YYYY-MM-DD.
data = yf.download(ticker, start = "YYYY-MM-DD", end = "YYYY-MM-DD") #Retrieves the Data from Yahoo Finance for the duration. 
#print(data.head()) #Prints the first 5 Instances the stock traded.


#Plotting the Graph of the stock within the set period.
data['Close'].plot(title=f" {info.get("longName")} Stock Price")
plt.xlabel("Date")
plt.ylabel(f"Price in {loc_currency}")
plt.grid()
plt.show()

print(ticker)