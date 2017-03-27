#!/usr/bin/python
#This script generate proten sequence from genbank in fasta form
#Usage: python genbank_to_faa.py genbankfile.gbk > output.faa

import sys
import gzip
from Bio import SeqIO

def main():
    if sys.argv[1][-2:] == 'gz':
        gb_file = gzip.open(sys.argv[1],'rb')
    else:
        gb_file = open(sys.argv[1],'r')

    for gb_record in SeqIO.parse(gb_file,"genbank") :
        genome_name = gb_record.name
        for feat in gb_record.features:
            if feat.type == "CDS":
                name = "unkown"
                if("locus_tag" in feat.qualifiers):
                    name = feat.qualifiers['locus_tag'][0]
                elif("gene" in feat.qualifiers):
                    name = feat.qualifiers['gene'][0]
                elif("db_xref" in feat.qualifiers):
                    name = feat.qualifiers['db_xref'][0]
                if ("translation" in feat.qualifiers):
                    print ">%s from %s\n%s" %(name,genome_name,feat.qualifiers['translation'][0])

if __name__ == '__main__':
    main()
