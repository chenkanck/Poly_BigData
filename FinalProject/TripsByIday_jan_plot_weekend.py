import matplotlib, sys ， time
matplotlib.use('Agg')
import matplotlib.pyplot as m_plot


if __name__=='__main__':
    counts = []
    with open(sys.argv[1], 'r') as f:
        for line in f:
            pair = line.strip().split('\t')
            day = time.strptime(pair[0], '%Y-%m-%d')
            pair[0] = day.tm_wday
            counts.append(map(int, pair))
    counts.sort()
    for a in counts:
        print a
    fig = m_plot.figure(figsize=(11, 4))
    fig.suptitle('Trips vs Time', fontsize=20)
    ax = fig.add_subplot(111, xticks = [1,2,3,4,5,6,7])
    # ax.plot_date(*zip(*counts), fmt='r-', aa=True)
    ax.plot(*zip(*counts))
    ax.set_ylim([0, 200000])
    fig.savefig(sys.argv[2])
