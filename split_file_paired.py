#!/usr/bin/python

#this script split one fastq file into two paired end file


import sys

he = sys.argv[1].split('.')[0]
r1 = open(he+"_1.fastq",'w')
r2 = open(he+"_2.fastq",'w')
s1 = open(he+"_single.fastq",'w')
r = 1

flag = 0
save1 = []
save2 = []
ini = 0
for n, line in enumerate(open(sys.argv[1],'r')):
    if n % 4 == 0:
        spl = line.strip().split(' ')
        if spl[len(spl)-1][0] == '1':
            if ini == 0:
                ini = 1
            else:
                if len(save2) == 0:
                    for x in save1:
                        s1.write(x)
                        save1 = []
                else:
                    for x in save1:
                        r1.write(x)
                        save1 = []
                    for x in save2:
                        r2.write(x)
                        save2 = []

            save1.append("@"+spl[1]+' '+spl[3]+'\n')
            r = 1

        else:
            save2.append("@"+spl[1]+' '+spl[3]+'\n')
            r = 2

    else:
        if r == 1:
            save1.append(line)
        else:
            save2.append(line)
