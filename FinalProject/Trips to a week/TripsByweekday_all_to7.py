import sys , time

#input format:    yday \t counts
#output format :   weekday \t average counts 

if __name__=='__main__':
    counts = {}
    day_count = {}
    with open(sys.argv[1], 'r') as f:
        for line in f:
            pair = line.strip().split('\t')
            year_day = '2013-'+pair[0]
            day = time.strptime(year_day, '%Y-%j')
            dkey = day.tm_wday
            if counts.has_key(dkey):
                value = counts[dkey]+int(pair[1])
                counts[dkey] = value
                day_count[dkey] = day_count[dkey]+1
            else:
                day_count[dkey]=1
                counts[dkey] = int(pair[1])

    # average
    for dday in counts:
        counts[dday] = counts[dday] / day_count[dday]




    fp = open("weekdays.txt",'w')
    for a in counts:
        out = str(a) + "\t"+str(counts[a])+'\n'
        print out
        fp.write(out)

    fp.close()
    