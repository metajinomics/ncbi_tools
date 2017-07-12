#!/usr/bin/python
#This script generate nucloetide sequence from genbank in fasta form
#gzip(gz) support
#Usage: python genbank_to_fna.py genbankfile.gbk > output.fna
#usage: python genbank_to_fna.py genbankfile.gbk.gz > output.fna

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
                prod = "unkown"
                if("locus_tag" in feat.qualifiers):
                    name = feat.qualifiers['locus_tag'][0]
                elif("gene" in feat.qualifiers):
                    name = feat.qualifiers['gene'][0]
                elif("db_xref" in feat.qualifiers):
                    name = feat.qualifiers['db_xref'][0]
                if ("product" in feat.qualifiers):
                    product = feat.qualifiers['product'][0]
                if ("translation" in feat.qualifiers):
                    print ">%s from %s %s\n%s" %(name,genome_name,product,feat.qualifiers['translation'][0])

if __name__ == '__main__':
    main()
