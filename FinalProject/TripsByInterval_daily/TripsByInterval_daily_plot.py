import matplotlib, sys
matplotlib.use('Agg')
import matplotlib.pyplot as m_plot
def parseTime(strtime):
    h_m = strtime.split(':')
    mins = (float(h_m[1]))/60
    mins = float ('%.2f' %mins)
    return int(h_m[0])+mins

if __name__=='__main__':
    counts = []
    with open(sys.argv[1], 'r') as f:
        for line in f:
            pair = line.strip().split('\t')
            pair[0] = parseTime(pair[0])
            pair[1] = int(pair[1]) / 365
            counts.append(map(float, pair))
    counts.sort()
    for a in counts:
        print a
    fig = m_plot.figure(figsize=(11, 4))
    fig.suptitle('Trips vs Time', fontsize=20)
    ax = fig.add_subplot(111, xticks = [2,4,6,8,10,12,14,16,18,20,22,24])
    # ax.plot_date(*zip(*counts), fmt='r-', aa=True)
    ax.plot(*zip(*counts))
    ax.set_ylim([0, 5000])
    fig.savefig(sys.argv[2])
