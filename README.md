# ncbi_tools
NCBI tools


### Ganbank to fasta

#### fetch fasta file with CDS from NCBI 
First, you need a file that contains NCBI ID that you want to fetch. If you filename is list_id.txt, then
```
python fetch_fasta_cds.py list_id.txt output_dir_name
```

#### genbank to nucleotide
gz file supported
```
python genbank_to_fna.py genbankfile.gbk > output.fna
```
#### genbank to protein sequence
```
python genbank_to_faa.py genbankfile.gbk > output.faa
```

### find nucloetide sequence from genbank in fasta form that matches EC number
#### nucleotide
```
python find_ec_fna_from_genbank.py genbankfile.gbk.gz 3.2.1.4> output.fna
```

#### protein
```
python find_ec_faa_from_genbank.py genbankfile.gbk.gz 3.2.1.4> output.faa
```

### For RefSeq Database
#### get link locus tag and protein ID
```
for x in *.gbff;do python get_link_locusTag_proteinID.py $x;done > link_locusTag_proteinID.txt
```

#### get nucleotide sequence for each gene from RefSeq database
```
for x in *.genomic.gbff.gz;do python /mnt/scratch/choiji22/ncbi_tools/genbank_to_ffn_refseq.py $x ${x%.genomic.gbff.gz*}.1.genomic.fna.gz > ${x%.gbff.gz}.ffn;done
```
