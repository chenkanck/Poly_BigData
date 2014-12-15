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
            
            srcDst = part[1]
            src_dst = srcDst.split('->')
            src= src_dst[0]
            
            print '%s\t%s' % (src, datas[1])
        except IndexError:
            pass