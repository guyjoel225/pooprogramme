
import time

import datetime


date = datetime.date(2010,10,25)

today = datetime.date.today()

tempstmp = time.time()

dates = datetime.date.fromtimestamp(tempstmp)

print(dates)




if dates == today:
    
    print(" la date est identique")
    
else:
    
    print("la date est differente")
    
    
now = datetime.datetime.now()

print(now)


tme = time.strftime("%A-%d-%B-%Y  %H:%M:%S")


print(tme)