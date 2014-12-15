#!/usr/bin/env python

import sys, time
#works on Trip_fare_#.csv
#   output of mapper:
#   10 mins interval counts
#   Format
#   year-month-day START to END , 1
# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    datas = line.split(',')
    if len(datas)>1 and datas[0]!='medallion':
        try :
            pickup_time = time.strptime(datas[3],'%Y-%m-%d %H:%M:%S')
            minute = pickup_time.tm_min
            block = (minute/10) * 10
            interval = str(pickup_time.tm_year)+'-'+str(pickup_time.tm_mon)+'-'\
                    +str(pickup_time.tm_mday)
            start =str(pickup_time.tm_hour)+':'+str(block) +':00'
            end = str(pickup_time.tm_hour)+':'+str(block+9)+':59'
            interval = interval+' '+start+' to '+end
            print '%s\t%s' % (interval, 1)
        except IndexError:
            pass