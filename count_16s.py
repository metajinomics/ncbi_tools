#!/usr/bin/python

import sys
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

def main():
    file = sys.argv[1]
    genome=SeqIO.read(file, 'genbank')
    n = 0
    l = []

    for record in list(SeqIO.parse(file, 'genbank')):
        org = record.annotations["source"]
        for feat in genome.features:
            if feat.type == "rRNA":
                if '16S' in feat.qualifiers['product'][0]:
                    n = n + 1
        print n

if __name__ == '__main__':
    main()
