#!/usr/bin/env python
import sys
sys.path.append('.')
import matplotlib
matplotlib.use('Agg')
from matplotlib.path import Path
from rtree import index as rtree
import numpy, shapefile, time

def findNeighborhood(location, index, neighborhoods):
    match = index.intersection((location[0], location[1], location[0], location[1]))
    for a in match:
        if any(map(lambda x: x.contains_point(location), neighborhoods[a][1])):
            return a
    return -1

def readNeighborhood(shapeFilename, index, neighborhoods):
    sf = shapefile.Reader(shapeFilename)
    for sr in sf.shapeRecords():
        if sr.record[1] not in ['New York', 'Kings', 'Queens', 'Bronx']: continue
        paths = map(Path, numpy.split(sr.shape.points, sr.shape.parts[1:]))
        bbox = paths[0].get_extents()
        map(bbox.update_from_path, paths[1:])
        index.insert(len(neighborhoods), list(bbox.get_points()[0])+list(bbox.get_points()[1]))
        neighborhoods.append((sr.record[3], paths))
    neighborhoods.append(('UNKNOWN', None))

def parseInput():
    for line in sys.stdin:
        line = line.strip('\n')
        values = line.split(',')
        if len(values)>1 and values[0]!='medallion': 
            yield values

def mapper():
    index = rtree.Index()
    neighborhoods = []
    readNeighborhood('ZillowNeighborhoods-NY.shp', index, neighborhoods)
    agg = {}
    # agg_d = {}
    for values in parseInput():
        try:
            pickup_time = time.strptime(values[5],'%Y-%m-%d %H:%M:%S')
            minute = pickup_time.tm_min
            block = (minute/10) * 10
            interval = str(pickup_time.tm_year)+'-'+str(pickup_time.tm_mon)+'-'\
                    +str(pickup_time.tm_mday)
            start =str(pickup_time.tm_hour)+':'+str(block) +':00'
            end = str(pickup_time.tm_hour)+':'+str(block+9)+':59'
            interval = interval+' '+start+' to '+end


            pickup_location = (float(values[10]), float(values[11]))
            drop_location = (float(values[12]),float(values[13]))
            pickup_neighborhood = findNeighborhood(pickup_location, index, neighborhoods)
            drop_neighborhood = findNeighborhood(drop_location, index, neighborhoods)
            if pickup_neighborhood!=-1 and drop_neighborhood!= -1:
                # agg[pickup_neighborhood] = agg.get(pickup_neighborhood, 0) + 1
                pick_nei = neighborhoods[pickup_neighborhood][0]
                drop_nei = neighborhoods[drop_neighborhood][0]
                src_dst = pick_nei+"->"+drop_nei
                # print '%s\t%s' % (s,1)
                s = interval + ','+ src_dst
                agg[s] = agg.get(s,0) + 1
        # if drop_neighborhood!=-1:
        #     agg_d[drop_neighborhood] = agg_d.get(drop_neighborhood , 0) + 1
        except ValueError:
        #     # print values
            pass
    for item in agg.iteritems():
        print '%s\t%s' % (item[0],item[1])
    # for item in agg.iteritems():
    #     print '%s\t%s' % (neighborhoods[item[0]][0], item[1])

if __name__=='__main__':
    mapper()
