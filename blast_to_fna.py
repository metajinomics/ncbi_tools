#!/usr/bin/python

# this script use blast output to find nucleotide sequences
# usage: python blast_to_fna.py blast ffn > output
# example: python blast_to_fna.py EC_3.2.1.21.out bacteria.555.genomic.ffn

import sys

def main():
    # read blast out
    d = {}
    blast = open(sys.argv[1],'r')
    for line in blast:
        spl = line.strip().split('\t')
        id = spl[1].split("|")[3]
        d[id] = line.strip()
    blast.close()
    # compare ffn
    ffn = open(sys.argv[2],'r')
    flag = 0
    for line in ffn:
        if line[:1] == ">":
            flag = 0
            id = line.split(' ')[1]
            if d.has_key(id):
                print line.strip()
                flag = 1
        else:
            if flag == 1:
                print line.strip()
            
        


if __name__ == "__main__":
    main()

