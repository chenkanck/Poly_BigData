#!/usr/bin/env python

import sys, time
#works on interval-src-dst (intermediate data)
#output the intervals in exact one neighborhood

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    datas = line.split('\t')
    # data[0] interval,src-dst
    # data[1] numbers
    if len(datas)>1:
        try :
            part = datas[0].split(',')
            interval = part[0]
            day_st_to_end = interval.split(' ')
            src_dst= part[1].split('->')
            src = src_dst[0]
            if src != 'Upper West Side':
                continue
            date = time.strptime(day_st_to_end[0],'%Y-%m-%d')
            if date.tm_mon != 8 or date.tm_mday!=1:
                continue
            # output_key
            print '%s\t%s' % (day_st_to_end[1], datas[1])
        except IndexError:
            pass