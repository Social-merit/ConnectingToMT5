from datetime import datetime
import MetaTrader5 as mt5
import pandas as pd
import authentication 
from authentication import authorized # Make sure authenticate.py

# Call without parameters. Return active orders on all symbols.
# orders_get()

# Call specifying a symbol active orders should be received for.
# orders_get(
#    symbol="SYMBOL"      // symbol name
# )

# Call specifying a group of symbols active orders should be received for.
# orders_get(
#    group="GROUP"        // filter for selecting orders for symbols
# )

# Call specifying the order ticket.
# orders_get(
#    ticket=TICKET        // ticket
# )


############################## orders_get ####################################################
# Get active orders with the ability to filter by symbol or ticket. There are three call options.
##################################################################################
# display data on active orders on GBPUSD
orders=mt5.orders_get(symbol="GBPUSD")
if orders is None:
    print("No orders on GBPUSD, error code={}".format(mt5.last_error()))
else:
    print("Total orders on GBPUSD:",len(orders))
    # display all active orders
    for order in orders:
        print(order)
print()
 
# get the list of orders on symbols whose names contain "*GBP*"
gbp_orders=mt5.orders_get(group="*GBP*")
if gbp_orders is None:
    print("No orders with group=\"*GBP*\", error code={}".format(mt5.last_error()))
else:
    print("orders_get(group=\"*GBP*\")={}".format(len(gbp_orders)))
    # display these orders as a table using pandas.DataFrame
    df=pd.DataFrame(list(gbp_orders),columns=gbp_orders[0]._asdict().keys())
    df.drop(['time_done', 'time_done_msc', 'position_id', 'position_by_id', 'reason', 'volume_initial', 'price_stoplimit'], axis=1, inplace=True)
    df['time_setup'] = pd.to_datetime(df['time_setup'], unit='s')
    print(df)
 



############################## orders_total ####################################################
# Get the number of active orders.
##################################################################################

# check the presence of active orders
orders=mt5.orders_total()
if orders>0:
    print("Total orders=",orders)
else:
    print("Orders not found")


# shut down connection to the MetaTrader 5 terminal
mt5.shutdown()