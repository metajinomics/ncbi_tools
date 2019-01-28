#!/usr/bin/python
#usage python SRR_from_SRP.py SRP.list

import urllib2
import os
import sys
import time

if len(sys.argv) != 2:
    print "USAGE: SRR_from_SRP.py <SRR_id_list> > output"
    sys.exit(1)

url_template = "http://trace.ncbi.nlm.nih.gov/Traces/sra/sra.cgi?save=efetch&db=sra&rettype=runinfo&term=%s"


for id in open(sys.argv[1]):
    id = id.strip()
    if id == "":
        continue


    csv = urllib2.urlopen(url_template % id).read()
    run_id = 0
    for n,line in enumerate(csv.split('\n')):
        spl = line.strip().split(',')
        if len(spl) < 2:
            continue
        if n == 0:
            for i,x in enumerate(spl):
                if x == "run":
                    run_id = i
            continue
        print spl[run_id]

    time.sleep(1.0/3)

