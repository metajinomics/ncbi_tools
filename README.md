# ncbi_tools
NCBI tools


### Ganbank to fasta
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
python genbank_to_fna.py genbankfile.gbk.gz 3.2.1.4> output.fna
```

#### protein
```
python genbank_to_faa.py genbankfile.gbk.gz 3.2.1.4> output.faa
```