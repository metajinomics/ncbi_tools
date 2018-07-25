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
        
        result =  [genome_name]
        result.append('\t'.join(gb_record.annotations['taxonomy']))

        print '\t'.join(result)
if __name__ == '__main__':
    main()
