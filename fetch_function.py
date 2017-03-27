#!/usr/bin/python

import sys
import time
from Bio import SeqIO
from Bio import Entrez

for id in open(sys.argv[1]):
    spl = id.strip().split('\t')
    id = spl[0]
    if id == "":
        continue
    
    start = int(spl[1])
    end = int(spl[2])

    Entrez.email = "genase23@gmail.com"
    handle = Entrez.efetch(db="nuccore",
                       id=id,
                       rettype="gb",
                       retmode="text")

    whole_sequence = SeqIO.parse(handle, "genbank")  
    for gb_record in whole_sequence:
        for feature in gb_record.features:
            if feature.type== "CDS" :
                fstart = int(feature.location.start)
                fend = int(feature.location.end)
                if (fstart < start and fstart < end and fend > start and fend > end):
                    result =  [str(gb_record.name), str(feature.qualifiers['locus_tag'][0]), str(feature.qualifiers['product'][0])]
                    print '\t'.join(result)
    time.sleep(1.0/3)
