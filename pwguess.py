from itertools import product
from time import time, sleep
import string
import os


def bruteforce(password, symbols):
	start = time()
	repeats = len(str(password))
	tuplist = (product(symbols, repeat=repeats))
	tries = 0
	endtime = 0
	for i in tuplist:
		tries += 1
		if "".join(list(i)) == password:
			endtime = (time()-start)
			return(endtime, tries)
			break

	return (-1, tries)

def getresults(start, end, symbols, charset, avgoverall, rawoverall, directory):
	print(charset)

	avgdata = open("results/"+charset+"results2", "w+")
	rawdata = open("rawdata/"+charset+"rawdata2", "w+")



	rawdata.write("Length,Symbols,Time,Variance\n")
	avgdata.write("Length,Symbols,Average_Time,Variance\n")

	averages = {}
	totalfailures = 0

	for i in range(start,end+1):
		print(i)
		stored = []
		averages[i] = [0,0,0]
		etime = 0
		tries = 0
		failures = 0

		newfile = open(directory+str(charset)+str(i), "r")

		for j in newfile.read().split("\n"):
			values = bruteforce(str(j), symbols)

			if values[0] > (-1):
				stored.append(etime)
				rawdata.write(str(i)+","+str(len(symbols))+","+str(etime)+","+str(tries)+"\n")
				rawoverall.write(str(i)+","+str(len(symbols))+","+str(etime)+","+str(tries)+"\n")

				etime += values[0]
				tries += values[1]

			else:
				failures += 1
		sqdiffs = 0		
		avgtime = etime/(100-failures)
		for k in stored:
			sqdiffs += (avgtime-k)*(avgtime-k)
		variance = sqdiffs/100

		totalfailures += failures
		averages[i] = [1000*(etime/100), tries/(100-failures), failures, variance]

		avgdata.write(str(i)+","+str(len(symbols))+","+str(averages[i][0])+","+str(averages[i][3])+"\n")
		avgoverall.write(str(i)+","+str(len(symbols))+","+str(averages[i][0])+","+str(averages[i][3])+"\n")

	avgdata.close()
	rawdata.close()

	print(averages)
	print(totalfailures)


rawoverall = open("rawdata/overall2", "w+")
avgoverall = open("results/overall2", "w+")
avgoverall.write("Length,Symbols,Average_Time,Variance\n")
rawoverall.write("Length,Symbols,Time,Tries\n")

if not os.path.exists("results"):
    os.makedirs("results")
if not os.path.exists("rawdata"):
    os.makedirs("rawdata")
for i in range(5,96,5):
	getresults(1,3, string.printable[0:i], str(i)+"_", avgoverall, rawoverall, "sympws/")



