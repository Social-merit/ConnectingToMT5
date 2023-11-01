
import MetaTrader5 as mt5
import os
import time
import pandas as pd
import authentication 
from authentication import authorized # Make sure authenticate.py is in the same directory as main.py


##################################################################################
# Returns a tuple from BookInfo featuring Market Depth entries for the specified symbol
##################################################################################

# subscribe to market depth updates for EURUSD (Depth of Market)
if authorized:
 
    if mt5.market_book_add('EURUSD'): # Subscribes the MetaTrader 5 terminal to the Market Depth change events for a specified symbol
        print("Market book 'EURUSD' is subscribed successfully")

        # get the market depth data 10 times in a loop
        time.sleep(1)
        for i in range(10):
                # get the market depth content (Depth of Market)
                items = mt5.market_book_get('EURUSD',  )
                # display the entire market depth 'as is' in a single string
                print(items)
                # now display each order separately for more clarity
                if items:
                    for it in items:
                        # order content
                        print(it._asdict())
                # pause for 5 seconds before the next request of the market depth data
                time.sleep(5)
        # cancel the subscription to the market depth updates (Depth of Market)
        mt5.market_book_release('EURUSD')
else:
    print("mt5.market_book_add('EURUSD') failed, error code =",mt5.last_error())



# shut down connection to the MetaTrader 5 terminal
mt5.shutdown()
