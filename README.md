# ncbi_tools
This repository provide useful tools for data of NCBI 

First, you need a file that contains NCBI ID that you want to fetch. If you filename is id_list.txt, then

### Download Genbank file
```
python fetch_genbank.py id_list.txt output_folder
```

### Download FASTA file
#### Download Full genome nucleotide seqeunce
```
python fetch_fasta_genome.py id_list.txt output_folder
```

#### Download feature gene (CDS) nucleotide sequence
```
python fetch_fasta_cds.py id_list.txt output_folder
```

#### Download feature gene (CDS) Protein amino-acid sequence
```
python fetch_fasta_protein.py id_list.txt output_folder
```

#### Download specific part of genome
In this case input file (id_list.txt) need to have three column (accession_ID, start position, end position) with tab separated value
```
python fetch_fasta_part.py id_list.txt output_folder
```

### Genbank to fasta
If you already have Genbank file, you can extract nucleotide sequence and/or amino-acid sequence. Note, you need to have FULL-VERSION of the file. If not, you won't be able to extract nucloetide sequence.
 

#### genbank to nucleotide
Note, gz file supported
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
