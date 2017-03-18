#!/usr/bin/env python2.7

#Program: datetime.py
#Author: Katie Lutz
#This program is evidence of executable code that was checked into our repository.
#
#The purpose of this program is to correctly identify the morning, afternoon, or
#night (time of day) that will aid the user in their initial preferences.

#from datetime import datetime #allows access to the .now() member function
import datetime

#TIME=str(datetime.now()) #human-readable date/time format
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


if WEEKDAY > 4:
  print 'It\'s the weekend!'
else:
  print 'Long work week?'

print DAY
