#!/usr/bin/python

#this script split one fastq file into two paired end file


import sys

he = sys.argv[1].split('.')[0]
r1 = open(he+"_1.fastq",'w')
r2 = open(he+"_2.fastq",'w')

r = 1
for n, line in enumerate(open(sys.argv[1],'r')):
    if n % 4 == 0:
        spl = line.strip().split(' ')
        if spl[len(spl)-1][0] == '1':
            r1.write("@"+spl[1]+' '+spl[3]+'\n')
            r = 1
        else:
            r2.write("@"+spl[1]+' '+spl[3]+'\n')
            r = 2
    else:
        if r == 1:
            r1.write(line)
        else:
            r2.write(line)
