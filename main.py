
import MetaTrader5 as mt5
import os

# display data on the MetaTrader 5 package
print("MetaTrader5 package author: ",mt5.__author__)
print("MetaTrader5 package version: ",mt5.__version__)

os.chdir(r"D:\App\Program\MQL5\Pratice")
key = open("./key.txt", "r").read().split()
# C:\Program Files\MetaTrader 5 IC Markets (SC)
path = r"C:\Program Files\MetaTrader 5 IC Markets (SC)\terminal64.exe"



# establish MetaTrader 5 connection to a specified trading account
if not mt5.initialize(path=path,  login=int(key[0]), password=key[1], server=key[2]):
    print("initialize() failed, error code =",mt5.last_error())

else:
    print("connection established to login #51438959")



