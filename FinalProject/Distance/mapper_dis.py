#!/usr/bin/env python
import sys, time,math

def parseInput():
    for line in sys.stdin:
        line = line.strip('\n')
        values = line.split(',')
        if len(values)>1 and values[0]!='medallion': 
            yield values

def mapper():
    agg = {}
    for values in parseInput():
        # values[5] is valid for trip_data.csv
        distance = float(values[9])
        key = str(math.ceil(distance))
        agg[key] = agg.get(key, 0) + 1

    for item in agg.iteritems():
        print '%s\t%s' % item

if __name__=='__main__':
    mapper()
