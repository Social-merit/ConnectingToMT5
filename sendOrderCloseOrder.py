import time
import MetaTrader5 as mt5
import pandas as pd # Import pandas module for displaying data obtained in the tabular form
import pytz # Import pytz module for working with time zone
import authentication 
from authentication import authorized # Make sure authenticate.py


############################## orders_send ####################################################
# Send a request to perform a trading operation from the terminal to the trade server. The function is similar to OrderSend.
##################################################################################


# prepare the buy request structure
symbol = "EURUSD"
symbol_info = mt5.symbol_info(symbol)
if symbol_info is None:
    print(symbol, "not found, can not call order_check()")
    mt5.shutdown()
    quit()
 
# if the symbol is unavailable in MarketWatch, add it
if not symbol_info.visible:
    print(symbol, "is not visible, trying to switch on")
    if not mt5.symbol_select(symbol,True):
        print("symbol_select({}}) failed, exit",symbol)
        mt5.shutdown()
        quit()
 
lot = 0.02 # lot size, 0.1 is the minimum allowed value, in units of the base currency, for example the euro, 
stoploss = 100 # stop loss size, in points
takeprofit = 100 # take profit size, in points
point = mt5.symbol_info(symbol).point
price = mt5.symbol_info_tick(symbol).ask
deviation = 10 # deviation from the current price
request = {
    "action": mt5.TRADE_ACTION_DEAL,
    "symbol": symbol,
    "volume": lot,
    "type": mt5.ORDER_TYPE_BUY,
    "price": price,
    "sl": price - int(stoploss) * point,
    "tp": price + int(takeprofit) * point,
    "deviation": deviation,
    "magic": 234000,
    "comment": "python script open order test",
    "type_time": mt5.ORDER_TIME_GTC,
    # "type_filling": mt5.ORDER_FILLING_RETURN,  # ic market only support IOC
    "type_filling": mt5.ORDER_FILLING_IOC,
}
 
# send a trading request
result = mt5.order_send(request)
# check the execution result
print("1. order_send(): by {} {} lots at {} with deviation={} points".format(symbol,lot,price,deviation));
if result.retcode != mt5.TRADE_RETCODE_DONE:
    print("2. order_send failed, retcode={}".format(result.retcode))
    # request the result as a dictionary and display it element by element
    result_dict=result._asdict()
    for field in result_dict.keys():
        print("   {}={}".format(field,result_dict[field]))
        # if this is a trading request structure, display it element by element as well
        if field=="request":
            traderequest_dict=result_dict[field]._asdict()
            for tradereq_filed in traderequest_dict:
                print("       traderequest: {}={}".format(tradereq_filed,traderequest_dict[tradereq_filed]))
    print("shutdown() and quit")
    # mt5.shutdown()
    # quit()
 
# print("2. order_send done, ", result)
# print("   opened position with POSITION_TICKET={}".format(result.order))
# print("   sleep 2 seconds before closing position #{}".format(result.order))
# # time.sleep(2)


############################## create a close request ####################################################
# # create a close request
# position_id=result.order
# price=mt5.symbol_info_tick(symbol).bid
# deviation=20
# request={
#     "action": mt5.TRADE_ACTION_DEAL,
#     "symbol": symbol,
#     "volume": lot,
#     "type": mt5.ORDER_TYPE_SELL,
#     "position": position_id,
#     "price": price,
#     "deviation": deviation,
#     "magic": 234000,
#     "comment": "python script close",
#     "type_time": mt5.ORDER_TIME_GTC,
#     "type_filling": mt5.ORDER_FILLING_RETURN,
# }
# # send a trading request
# result=mt5.order_send(request)
# # check the execution result
# print("3. close position #{}: sell {} {} lots at {} with deviation={} points".format(position_id,symbol,lot,price,deviation));
# if result.retcode != mt5.TRADE_RETCODE_DONE:
#     print("4. order_send failed, retcode={}".format(result.retcode))
#     print("   result",result)
# else:
#     print("4. position #{} closed, {}".format(position_id,result))
#     # request the result as a dictionary and display it element by element
#     result_dict=result._asdict()
#     for field in result_dict.keys():
#         print("   {}={}".format(field,result_dict[field]))
#         # if this is a trading request structure, display it element by element as well
#         if field=="request":
#             traderequest_dict=result_dict[field]._asdict()
#             for tradereq_filed in traderequest_dict:
#                 print("       traderequest: {}={}".format(tradereq_filed,traderequest_dict[tradereq_filed]))
 
# shut down connection to the MetaTrader 5 terminal
mt5.shutdown()


