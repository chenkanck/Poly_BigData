import os
import sys
# aggregate files in one txt
def writeData (files,output):

	fp = open(output,"w")
	for f in files:
		fpt = open(f,"r")
		for line in fpt:
			fp.write(line)
	fp.close

def aggregate(root):
	list_dirs = os.walk(root)
	names = []
	for root,dirs, files in list_dirs:
		for f in files:
			f = os.path.join(root,f)
			names.append(f)
	return names


if __name__== '__main__':
	rt = sys.argv[1]
	names = aggregate(rt)

	output = os.path.join(rt,"out.txt")
	writeData(names,output)