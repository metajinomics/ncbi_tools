#!/usr/bin/python

import urllib2
import os
import sys
import time

if len(sys.argv) != 3:
    print "USAGE: fetch_genome.py <genome_id_list> <out_dir>"
    sys.exit(1)

#url_template = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nucleotide&id=%s&rettype=fasta&retmode=text"
url_template = "https://www.ncbi.nlm.nih.gov/sviewer/viewer.cgi?tool=portal&save=file&log$=seqview&db=nuccore&report=gff3&sort=&id=%s&from=begin&to=end&extrafeat=976&fmt_mask=294912&maxplex=3"

os.mkdir(sys.argv[2])

for id in open(sys.argv[1]):
    id = id.strip()
    if id == "":
        continue

    sys.stdout.write("Fetching %s..." % id)
    sys.stdout.flush()
    gbk_out_file = os.path.join(sys.argv[2], id + ".gff3")
    if os.path.exists(gbk_out_file):
        print "already fetched"

    open(gbk_out_file, "w").write(urllib2.urlopen(url_template % id).read())
    print "Done"
    time.sleep(1.0/3)

