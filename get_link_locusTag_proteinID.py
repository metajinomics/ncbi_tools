#!/usr/bin/python

# this script make link between protein_id and locus_tag in genbank file
# usage: python get_link_proteinID_locusTag.py genbankfile > output
# example: for x in *.gbff;do python get_link_proteinID_locusTag.py $x;done > output
# example: for x in *.gbff;do python get_line_proteinID_locusTag.py $x > $x.link;done 

import sys
import gzip
from Bio import SeqIO

def main():
    print "here"
    if sys.argv[1][-2:] == 'gz':
        gb_file = gzip.open(sys.argv[1],'rb')
    else:
        gb_file = open(sys.argv[1],'r')

    for gb_record in SeqIO.parse(gb_file,"genbank") :
        #genome_name = gb_record.name
        for feat in gb_record.features:
            if feat.type == "CDS":
                locus = "unkown"
                pro = "unkown"
                if("locus_tag" in feat.qualifiers):
                    locus = feat.qualifiers['locus_tag'][0]
                elif("gene" in feat.qualifiers):
                    locus = feat.qualifiers['gene'][0]
                
                if("protein_id" in feat.qualifiers):
                    pro = feat.qualifiers['protein_id'][0]
                else:
                    pro = "NA"
                print "%s\t%s" %(locus, pro)



if __name__ == "__main__":
    main()
