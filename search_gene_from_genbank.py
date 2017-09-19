#!/usr/bin/python
"""
This script search gene in 'product' from genbank file
usage: python search_gene_from_genbank.py name_of_gene genbank.gbk nucl/prot
example: python search_gene_from_genbank.py McyA xxx.gbk > output.txt
"""

import sys
import gzip
from Bio import SeqIO

def main():
    gene_name = sys.argv[1]
    filename = sys.argv[2]
    handle = sys.argv[3]
    if filename[-2:] == 'gz':
        gb_file = gzip.open(filename,'rb')
    else:
        gb_file = open(filename,'r')

    for gb_record in SeqIO.parse(gb_file,"genbank") :
        genome_name = gb_record.name
        for feat in gb_record.features:
            if feat.type == "CDS":
                name = "unkown"
                if("product" in feat.qualifiers):
                    if gene_name in feat.qualifiers['product'][0] :
                        if("locus_tag" in feat.qualifiers):
                            name = feat.qualifiers['locus_tag'][0]
                        elif("gene" in feat.qualifiers):
                            name = feat.qualifiers['gene'][0]
                        if handle == "nucl":
                            print ">%s from %s\n%s" %(name,genome_name,feat.extract(gb_record.seq))
                        else:
                            print ">%s from %s\n%s" %(name,genome_name,feat.qualifiers['translation'][0])

if __name__ == '__main__':
    main()
