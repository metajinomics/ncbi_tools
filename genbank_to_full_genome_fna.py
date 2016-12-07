#!/usr/bin/python

#this script generate full genome nucleotide sequence
# usage: python genbank_to_full_genome_fna.py gengank.gbk > fullgenome.fna

import sys
from Bio import SeqIO

genbankfile = sys.argv[1]
genbank = open(genbankfile, 'r')

for seq_record in SeqIO.parse(genbank, "genbank"):
    print ">%s %s\n%s" %(seq_record.id, seq_record.description, seq_record.seq)

genbank.close()
