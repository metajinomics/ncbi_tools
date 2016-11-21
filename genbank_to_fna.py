#!/usr/bin/python
#This script generate nucloetide sequence from genbank in fasta form
#Usage: python genbank_to_fna.py genbankfile.gbk > output.fna

import sys
from Bio import SeqIO

def main():
    gb_file = sys.argv[1]
    for gb_record in SeqIO.parse(open(gb_file,'r'),"genbank") :
        genome_name = gb_record.name
        for feat in gb_record.features:
            if feat.type == "CDS":
                name = "unkown"
                if("locus_tag" in feat.qualifiers):
                    name = feat.qualifiers['locus_tag'][0]
                elif("gene" in feat.qualifiers):
                    name = feat.qualifiers['gene'][0]
                print ">%s from %s\n%s" %(name,genome_name,feat.extract(gb_record.seq))

if __name__ == '__main__':
    main()
