#!/usr/bin/python

#this script will get all taxonomy rank for all available
#usage: python get_taxonomy_all.py categories.dmp > full_tax_table.txt

import sys
import taxonomy_finder
import time

for line in open(sys.argv[1],'r'):
    spl = line.strip().split('\t')
    if len(spl) > 2:
        tax = taxonomy_finder.get_taxonomy(spl[2])
    else:
        tax = ["null","null","null","null","null","null","null"]
    #print tax
    print spl[2]+'\t'+ '\t'.join(tax)
    time.sleep(1.0/3)
