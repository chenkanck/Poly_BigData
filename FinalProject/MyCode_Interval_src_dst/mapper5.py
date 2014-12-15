#!/usr/bin/env python

import sys, time
#works on interval-src-dst (intermediate data)
#aggregate intervals into season,number format

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
            day_time = time.strptime(day_st_to_end[0],'%Y-%m-%d')
            season = ((day_time.tm_mon)%12)/3
            # 0,1,2,3 winter spring summer fall
            srcDst = part[1]
            src_dst = srcDst.split('->')
            dst= src_dst[1]
            output_key = str(season)+','+dst
            print '%s\t%s' % (output_key, datas[1])
        except IndexError:
            pass