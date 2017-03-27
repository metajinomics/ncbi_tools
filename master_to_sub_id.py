#!/usr/bin/python

import urllib2
import os
import sys
import time

if len(sys.argv) != 3:
    print "USAGE: fetch_genome.py <genome_id_list> <out_dir>"
    sys.exit(1)

#url_template = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nucleotide&id=%s&rettype=gb&retmode=text"
url_template = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=%s&rettype=gbwithparts&retmode=text"

os.mkdir(sys.argv[2])

for id in open(sys.argv[1]):
    id = id.strip()
    if id == "":
        continue

    gb = urllib2.urlopen(url_template % id).read()
    spl = gb.split('\n')
    for line in spl:
        if line[:3] == "WGS":
            sp = line.split("         ")[1].split('-')
            id1 = sp[0]
            header = id1[:len(id1)-7]
            id1_num = int(id1[len(id1)-7:])
            
            
            id2 = sp[1]
            id2_num = int(id2[len(id2)-7:])
            
            for i in range(id1_num,id2_num+1):
                print header + str(i)


    time.sleep(1.0/3)
