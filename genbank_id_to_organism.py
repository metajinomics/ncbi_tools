#!/usr/bin/python

import urllib2
import os
import sys
import time

if len(sys.argv) != 2:
    print "USAGE: fetch_genome.py <genome_id_list> > output.txt"
    sys.exit(1)

url_template = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nucleotide&id=%s&rettype=gb&retmode=text"
#url_template = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=%s&rettype=gbwithparts&retmode=text"

for id in open(sys.argv[1]):
    id = id.strip()
    if id == "":
        continue
    genbank = urllib2.urlopen(url_template % id).read()
    spl = genbank.split('\n')
    flag = 0
    for n,line in enumerate(spl):
        if n == 0:
            print line
        if "ORGANISM" in line:
            print line
            flag = 1 
            continue
        if flag == 1:
            print line
            flag = 0
            if line[-1] == ';':
                flag = 1
            else:
                break

    #time.sleep(1.0/3)

