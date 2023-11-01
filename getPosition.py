import MetaTrader5 as mt5
import os
import pandas as pd
# import authentication 
from authentication import authorized # Make sure authenticate.py
# authentication

######################## order_check #####################################################
# Check funds sufficiency for performing a required trading operation. Check result are returned as the MqlTradeCheckResult structure.
################################################################################## ######

# get account currency
account_currency=mt5.account_info().currency
print("Account currency:",account_currency)
 

# check the presence of open positions
positions_total=mt5.positions_total()
if positions_total>0:
    print("Total positions=",positions_total)
else:
    print("Positions not found")
 

 
# get open positions on USDCHF
positions=mt5.positions_get(symbol="USDJPY")
if positions==None:
    print("No positions on USDJPY, error code={}".format(mt5.last_error()))
elif len(positions)>0:
    print("Total positions on USDJPY =",len(positions))
    # display all open positions
    for position in positions:
        print(position)
 
# get the list of positions on symbols whose names contain "*USD*"
usd_positions=mt5.positions_get(group="*USD*")
if usd_positions==None:
    print("No positions with group=\"*USD*\", error code={}".format(mt5.last_error()))
elif len(usd_positions)>0:
    print("positions_get(group=\"*USD*\")={}".format(len(usd_positions)))
    # display these positions as a table using pandas.DataFrame
    df=pd.DataFrame(list(usd_positions),columns=usd_positions[0]._asdict().keys())
    df['time'] = pd.to_datetime(df['time'], unit='s')
    df.drop(['time_update', 'time_msc', 'time_update_msc', 'external_id'], axis=1, inplace=True)
    print(df)
