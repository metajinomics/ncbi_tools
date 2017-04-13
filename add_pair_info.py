#!/usr/bin/python

#this script add paired info at the end of the sequence name, assuming sequences are in order 1 and 2 or F and R

#usage: python add_pair_info.py SRR3452820.fastq > SRR3452820_paired.fastq

import sys

prev = ''
for n, line in enumerate(open(sys.argv[1],'r')):
    if n % 4 == 0 :
        spl = line.strip().split(' ')
        if spl[1] == prev:
            print line.strip() + " 2:N:0"
        else:
            print line.strip() + " 1:N:0"
            prev = spl[1]
    else:
        print line,
