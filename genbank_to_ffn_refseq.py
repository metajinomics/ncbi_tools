#!/usr/bin/python

# this script generage nucleotide sequence of each gene from genbank file in RefSeq which gbff and fna are present separately
# usage: python genbank_to_ffn_refseq.py genbank.gbff fasta.fna > output.ffn

import sys
import gzip
from Bio import SeqIO
import utils

def main():
    fasta = utils.read_fasta_refseq(sys.argv[2])
    if sys.argv[1][-2:] == 'gz':
        gb_file = gzip.open(sys.argv[1],'rb')
    else:
        gb_file = open(sys.argv[1],'r')

    for gb_record in SeqIO.parse(gb_file,"genbank") :
        genome_name = gb_record.name
        for feat in gb_record.features:
            if feat.type == "CDS":
                name = "unkown"
                pro = "unkown"
                if("locus_tag" in feat.qualifiers):
                    name = feat.qualifiers['locus_tag'][0] 
                elif("gene" in feat.qualifiers):
                    name = feat.qualifiers['gene'][0]
                if("protein_id" in feat.qualifiers):
                    pro = feat.qualifiers['protein_id'][0]
                else:
                    pro = "NA"

                start = feat.location.start
                end = feat.location.end
                strand = feat.location.strand
                seq = fasta[genome_name][start:end]
                
                if (strand == -1):
                    seq = utils.get_rc(seq)
                print ">%s %s from %s\n%s" %(name,pro,genome_name,seq)

if __name__ == '__main__':
    main()
