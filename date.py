#!/usr/bin/env python2.7

#Program: datetime.py
#Author: Katie Lutz
#This program is evidence of executable code that was checked into our repository.
#
#The purpose of this program is to correctly identify the morning, afternoon, or
#night (time of day) that will aid the user in their initial preferences.

import datetime
import time

WEEKDAY=datetime.datetime.today().weekday()

if WEEKDAY==0:
  DAY='Monday'
elif WEEKDAY==1:
  DAY='Tuesday'
elif WEEKDAY==2:
  DAY='Wednesday'
elif WEEKDAY==3:
  DAY='Thursday'
elif WEEKDAY==4:
  DAY='Friday'
elif WEEKDAY==5:
  DAY='Saturday'
else:
  DAY='Sunday'

print 'Today is',DAY
if WEEKDAY > 4:
  print 'It\'s the weekend!'
else:
  print 'Long work week?'

TIMEODAY=time.strftime("%H") #gets the hour of the day

HOUR = int(TIMEODAY)


#print message for appropriate time of day
if HOUR >= 12:
  if HOUR < 18:
    print 'Good afternoon!'
  else:
    print 'Are you looking for something to watch tonight?'
else:
  if HOUR > 6:
    print 'Good morning!'
  else:
    print 'Late night?'



