import sys
if __name__=='__main__':
    counts = []
    with open('out.txt', 'r') as f:
        for line in f:
            name, value = line.strip().split('\t')
            counts.append((int(value), name))
    counts.sort(reverse=True)
    counts = counts[:10]
    values, names = zip(*counts)
    fp = open ('out_sorted.txt','w')
    for i in range(len(values)):
        fp.write('%s\t%s\n' %(names[i],values[i]))

    # yticks = map(lambda x: len(counts)-x-0.5,range(len(names)))
    # fig = m_plot.figure(figsize=(7, 8))
    # fig.suptitle('Trips per Neighborhood daily', fontsize=20)
    # ax = m_plot.Axes(fig, [.3,.1,.6,.8])
    # fig.add_axes(ax) 
    # ax.barh(yticks, values, align='center')
    # m_plot.yticks(yticks, names)
    # fig.savefig(sys.argv[2])