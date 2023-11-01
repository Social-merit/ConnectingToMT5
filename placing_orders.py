
import MetaTrader5 as mt5
import os


os.chdir(r"D:\App\Program\MQL5\Pratice")
key = open("./key.txt", "r").read().split()
# C:\Program Files\MetaTrader 5 IC Markets (SC)
path = r"C:\Program Files\MetaTrader 5 IC Markets (SC)\terminal64.exe"


# establish MetaTrader 5 connection to a specified trading account
if mt5.initialize(path=path,login=int(key[0]), password=key[1], server=key[2]):
    print("connection established")

def place_market_order(symbol,vol,buy_sell,sl_pip,tp_pip):
    pip_unit = 10*mt5.symbol_info(symbol).point
    price = mt5.symbol_info_tick(symbol).ask
    if buy_sell.capitalize()[0] == "B":
        direction = mt5.ORDER_TYPE_BUY
        sl = price - sl_pip*pip_unit
        tp = price + tp_pip*pip_unit
    else:
        direction = mt5.ORDER_TYPE_SELL
        sl = price + sl_pip*pip_unit
        tp = price - tp_pip*pip_unit
    
    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": vol,
        "type": direction,
        "price": price,
        "sl": sl,
        "tp":tp,
        "type_time": mt5.ORDER_TIME_GTC,
        # "type_filling": mt5.ORDER_FILLING_RETURN,
        "type_filling": mt5.ORDER_FILLING_IOC,
    }
    
    result = mt5.order_send(request)
    print(result)
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
    return result

place_market_order("USDJPY",0.05,"BUY", 50,50)



# def place_limit_order(symbol,vol,buy_sell,pips_away):
    
#     pip_unit = 10*mt5.symbol_info(symbol).point
    
#     if buy_sell.capitalize()[0] == "B":
#         direction = mt5.ORDER_TYPE_BUY_LIMIT
#         price = mt5.symbol_info_tick(symbol).ask - pips_away*pip_unit
#     else:
#         direction = mt5.ORDER_TYPE_SELL_LIMIT
#         price = mt5.symbol_info_tick(symbol).ask + pips_away*pip_unit
        
    
    
#     request = {
#         "action": mt5.TRADE_ACTION_PENDING,
#         "symbol": symbol,
#         "volume": vol,
#         "type": direction,
#         "price": price,
#         "type_time": mt5.ORDER_TIME_GTC,
#         "type_filling": mt5.ORDER_FILLING_RETURN,
#     }
    
#     result = mt5.order_send(request)
#     return result
    
    
# place_limit_order("GBPUSD",0.02,"Buy",8)
