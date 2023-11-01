
from datetime import datetime
import MetaTrader5 as mt5
import pandas as pd # Import pandas module for displaying data obtained in the tabular form
import pytz # Import pytz module for working with time zone
import authentication 
from authentication import authorized # Make sure authenticate.py

pd.set_option('display.max_columns', 500) # number of columns to be displayed
pd.set_option('display.width', 1500)      # max table width to display


############################ copy_rates_from ######################################################
# Get bars from the MetaTrader 5 terminal starting from the specified date.
##################################################################################

# set time zone to UTC
timezone = pytz.timezone("Etc/UTC")
# create 'datetime' object in UTC time zone to avoid the implementation of a local time zone offset
utc_from = datetime(2020, 1, 10, tzinfo=timezone)
# get 10 EURUSD H4 bars starting from 01.10.2020 in UTC time zone
# https://www.mql5.com/en/docs/python_metatrader5/mt5copyratesfrom_py#timeframe - timeframes available
rates = mt5.copy_rates_from("EURUSD", mt5.TIMEFRAME_H4, utc_from, 10)
 
# shut down connection to the MetaTrader 5 terminal
# mt5.shutdown()

# display each element of obtained data in a new line
print("Display obtained data 'as is'")
# for rate in rates:
#     print(rate)
 
# create DataFrame out of the obtained data
rates_frame = pd.DataFrame(rates)
# convert time in seconds into the datetime format
rates_frame['time']=pd.to_datetime(rates_frame['time'], unit='s')
                           
# display data
print("\nDisplay dataframe with data")
print(rates_frame)

############################## copy_rates_from_pos ####################################################
# Get bars from the MetaTrader 5 terminal starting from the specified index
##################################################################################

# get 10 GBPUSD D1 bars from the current day
rates = mt5.copy_rates_from_pos("GBPUSD", mt5.TIMEFRAME_D1, 0, 10)
 
# shut down connection to the MetaTrader 5 terminal
# mt5.shutdown()

# display each element of obtained data in a new line
print("Display obtained data 'as is'")
# for rate in rates:
    # print(rate)
 
# create DataFrame out of the obtained data
rates_frame = pd.DataFrame(rates)
# convert time in seconds into the datetime format
rates_frame['time']=pd.to_datetime(rates_frame['time'], unit='s')
 
# display data
print("\nDisplay dataframe with data")
print(rates_frame) 

############################## copy_rates_range ####################################################
# Get bars from the MetaTrader 5 terminal starting from the specified index
##################################################################################

# set time zone to UTC
timezone = pytz.timezone("Etc/UTC")
# create 'datetime' objects in UTC time zone to avoid the implementation of a local time zone offset
utc_from = datetime(2023, 1, 10, tzinfo=timezone)
utc_to = datetime(2023, 1, 11, hour = 13, tzinfo=timezone)
# get bars from USDJPY M5 within the interval of 2020.01.10 00:00 - 2020.01.11 13:00 in UTC time zone
rates = mt5.copy_rates_range("USDJPY", mt5.TIMEFRAME_M5, utc_from, utc_to)
 
# shut down connection to the MetaTrader 5 terminal
# mt5.shutdown()
 
# display each element of obtained data in a new line
# print("Display obtained data 'as is'")
# counter=0
# for rate in rates:
#     counter+=1
#     if counter<=10:
#         print(rate)
 
# create DataFrame out of the obtained data
rates_frame = pd.DataFrame(rates)
# convert time in seconds into the 'datetime' format
rates_frame['time']=pd.to_datetime(rates_frame['time'], unit='s')
 
# display data
print("\nDisplay dataframe with data")
print(rates_frame.head(10))



############################## copy_ticks_from ####################################################
# Get bars from the MetaTrader 5 terminal starting from the specified index
##################################################################################

# set time zone to UTC
timezone = pytz.timezone("Etc/UTC")
# create 'datetime' object in UTC time zone to avoid the implementation of a local time zone offset
utc_from = datetime(2023, 1, 10, tzinfo=timezone)


# request 100 000 EURUSD ticks starting from 10.01.2019 in UTC time zone
# TICK_FLAG defines possible flags for ticks.
# These flags are used to describe ticks obtained
# by the copy_ticks_from() and copy_ticks_range() functions.
# https://www.mql5.com/en/docs/python_metatrader5/mt5copyticksfrom_py
ticks = mt5.copy_ticks_from("EURUSD", utc_from, 100000, mt5.COPY_TICKS_ALL)
# print("Ticks received:",len(ticks))
 
# shut down connection to the MetaTrader 5 terminal
# mt5.shutdown()
 
# display data on each tick on a new line
print("Display obtained ticks 'as is'")
count = 0
for tick in ticks:
    count+=1
    print(tick)
    if count >= 10:
        break
 
# create DataFrame out of the obtained data
ticks_frame = pd.DataFrame(ticks)
# convert time in seconds into the datetime format
ticks_frame['time']=pd.to_datetime(ticks_frame['time'], unit='s')
 
# display data
print("\nDisplay dataframe with ticks")
print(ticks_frame.head(10))



############################## copy_ticks_range ####################################################
# Get ticks for the specified date range from the MetaTrader 5 terminal.
##################################################################################
# set time zone to UTC
timezone = pytz.timezone("Etc/UTC")
# create 'datetime' objects in UTC time zone to avoid the implementation of a local time zone offset
utc_from = datetime(2023, 1, 10, tzinfo=timezone)
utc_to = datetime(2023, 1, 11, tzinfo=timezone)
# request AUDUSD ticks within 11.01.2020 - 11.01.2020
ticks = mt5.copy_ticks_range("AUDUSD", utc_from, utc_to, mt5.COPY_TICKS_ALL)
# print("Ticks received:",len(ticks))
 
# shut down connection to the MetaTrader 5 terminal
mt5.shutdown()
 
# display data on each tick on a new line
print("Display obtained ticks 'as is'")
count = 0
for tick in ticks:
    count+=1
    print(tick)
    if count >= 10:
        break
 
# create DataFrame out of the obtained data
ticks_frame = pd.DataFrame(ticks)
# convert time in seconds into the datetime format
ticks_frame['time']=pd.to_datetime(ticks_frame['time'], unit='s')
 
# display data
print("\nDisplay dataframe with ticks")
print(ticks_frame.head(10))