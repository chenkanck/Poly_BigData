#!/usr/bin/env python

import sys, time
#works on interval-src-dst (intermediate data)
#   output format:
#   daily interval / counts

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    datas = line.split('\t')
    # datas[0] interval,src-dst
    # datas[1] numbers
    if len(datas)>1:
        try :
            part = datas[0].split(',')
            # part[0] interval
            # part[1] src-dst
            interval = part[0]
            day_st_to_end = interval.split(' ')
            # start_time = time.strptime(day_st_to_end[1],'%H:%M:%S')
            # day_hour = start_time.tm_hour
            # day_min = start_time.tm_min
            
            # output_key = str(season)+','+dst
            
            print '%s\t%s' % (day_st_to_end[1], datas[1])
        except IndexError:
            pass