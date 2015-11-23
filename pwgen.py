import string
from random import randrange


def writefile(length, number, charset, charsetname):
	
		newstr = ("sympws/"+charsetname+str(length))
		newfile = open(newstr, "w+")
		
		for i in range(0,number):
			pw = []
			for j in range(0,length):
				pw.append(charset[randrange(0,len(charset))])
			newfile.write("".join(pw)+"\n")


for i in range(1,6):
	for j in range(5,96,5):
		charset = string.printable[0:j]
		writefile(i, 100, charset, str(j)+"_")