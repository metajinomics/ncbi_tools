#!/usr/bin/python
#this script remove return in fasta sequence

import sys

seq = []
flag = 0
for line in open(sys.argv[1],'r'):
    if line[:1] == ">":
        if flag == 0:
            print line,
        else:
            print ''.join(seq)
            seq = []
            print line,
    else:
        seq.append(line.strip())
print ''.join(seq)
