#!/usr/bin/env python

import sys, time
#works on interval 10mins (intermediate data)
#aggregate intervals into a daily format

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    datas = line.split('\t')
    # data[0] interval
    # data[1] numbers
    if len(datas)>1:
        try :
            part = datas[0].split(' ')

            interval = part[1]
            print '%s\t%s' % (interval, datas[1])
        except IndexError:
            pass