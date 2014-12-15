
fp = open("out.txt",'r')
fp1 = open ('winter.txt','w')
fp2 = open ('spring.txt','w')
fp3 = open ('summer.txt','w')
fp4 = open ('fall.txt','w')

day_winter = 90
day_spring = 92
day_summer = 92
day_fall = 91
for line in fp:
	parts = line.split('\t')
	
	values = parts[0].split(',')

	times = parts[1]
	season = values[0]
	dst = values[1]

	
	if int(season)==0:
		out = dst+'\t'+str((int(times))/day_winter)+'\n'
		fp1.write(out)
	elif int(season) == 1:
		out = dst+'\t'+str((int(times))/day_spring)+'\n'
		fp2.write(out)
	elif int(season) == 2:
		out = dst+'\t'+str((int(times))/day_summer)+'\n'
		fp3.write(out)
	else :
		out = dst+'\t'+str((int(times))/day_fall)+'\n'
		fp4.write(out)

fp1.close()
fp2.close()
fp3.close()
fp4.close()