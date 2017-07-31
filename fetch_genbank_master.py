#!/usr/bin/python

"""A script to fetch genbank file from NCBI,
when sequence ID is master record of shotgun sequencing
Try running this script from the command line like this:
  python fetch_genbank_master.py master_id
It will generate folder with id of record 
then download all genbank files into each folder

usage: python fetch_genbank_master.py master_id
example: python fetch_genbank_master.py NZ_AVNY00000000.1
"""


import urllib2
import os
import sys
import time

def get_genbank(folder_name,id):
    url_template = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=%s&rettype=gbwithparts&retmode=text"
    gbk_out_file = os.path.join(folder_name, id + ".gbk")
    if os.path.exists(gbk_out_file):
        print "already fetched"

    open(gbk_out_file, "w").write(urllib2.urlopen(url_template % id).read())
    time.sleep(1.0/3)

def get_id(id):
    url_template = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=%s&rettype=gbwithparts&retmode=text"
    gb = urllib2.urlopen(url_template % id).read()
    spl = gb.split('\n')
    ids = []
    for line in spl:
        if line[:3] == "WGS" and line[:4] != "WGS_":
            sp = line.split("         ")[1].split('-')
            if len(sp)>1 and sp[0][:2] != "NZ":
                id1 = sp[0]
                header = id1[:len(id1)-7]
                id1_num = int(id1[len(id1)-7:])
            
                id2 = sp[1]
                id2_num = int(id2[len(id2)-7:])
            
                for i in range(id1_num,id2_num+1):
                    ids.append(header + str(i))
    time.sleep(1.0/3)    
    return ids

def main():
    #check input format
    if len(sys.argv) != 2:
        print "USAGE: fetch_genbank_master.py <genome_master_id>"
        sys.exit(1)

    master = sys.argv[1]
    os.mkdir(master)
    ids = get_id(master)
    for each_id in ids:
        get_genbank(master,each_id)

if __name__ == '__main__':
    main()
