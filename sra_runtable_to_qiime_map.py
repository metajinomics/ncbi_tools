#!/usr/bin/python

#usage: 

import sys
Run_s = 0
Sample_Name_s = 0
for n,line in enumerate(open(sys.argv[1],'r')):
    spl = line.strip().split('\t')
    if n == 0:
        Run_s = [i for i, s in enumerate(spl) if 'Run_s' in s]
        Sample_Name_s = [i for i, s in enumerate(spl) if 'Sample_Name_s' in s]
        print "#SampleID\tRun_s"
    else:
        print spl[Sample_Name_s[0]]+'\t'+spl[Run_s[0]]
