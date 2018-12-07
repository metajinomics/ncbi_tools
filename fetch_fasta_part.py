#!/usr/bin/python

import urllib2
import os
import sys
import time
from string import maketrans

def get_rc(seq):
    seq = seq.upper()
    trans = maketrans("AGCT","TCGA")
    if isinstance(seq, unicode):
        seq = seq.encode("ascii")
    seq = seq.translate(trans)
    seq = seq[::-1]
    return seq

if len(sys.argv) != 3:
    print "USAGE: fetch_fasta_part.py <genome_id_list> <out_dir>"
    sys.exit(1)

url_template = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nucleotide&id={0}&seq_start={1}&seq_stop={2}&rettype=fasta&retmode=text"

if os.path.exists(sys.argv[2]):
    print "path exists"
else :
    os.mkdir(sys.argv[2])

for id in open(sys.argv[1]):
    id = id.strip()
    line = id
    if id == "":
        continue

    words = line.strip().split('\t')
    id = words[0]
    s1 = url_template.format(words[0],words[1],words[2])

    sys.stdout.write("Fetching %s..." % id)
    sys.stdout.flush()
    gbk_out_file = os.path.join(sys.argv[2], id +words[1]+ ".fa")

    if os.path.exists(gbk_out_file):
        print "already fetched"
    else :
        seq = urllib2.urlopen(s1).read()
        if(words[3] == "minus" or words[3] == "-"):
            seq = reverse_complement.get_from_url(seq)
        open(gbk_out_file, "w").write(seq)
        
    print "Done"
    time.sleep(1.0/3)
