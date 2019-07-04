"""
usage:
python gene_id_to_seq.py 3683 > 3683.fasta
"""


import sys
from urllib.request import urlopen
import xml.etree.ElementTree as ET

def fetch_fasta(locus_id):
    url_template = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nucleotide&id={0}&rettype=fasta&retmode=text"
    s1 = url_template.format(locus_id)
    seq = urlopen(s1).read().decode('utf-8')
    print(seq)

def find_refseq_selected(one_id):
    url_template = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id={0}&rettype=gb&retmode=text"
    s1 = url_template.format(one_id)
    seq = urlopen(s1).read().decode('utf-8')
    for line in seq.split('\n'):
        if 'KEYWORDS' in line:
            if 'RefSeq Select' in line:
                return True
            else:
                return False

def get_gene_summary(gene_id):
    url_template = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=gene&id={0}&retmode=xml"
    s1 = url_template.format(gene_id)
    seq = urlopen(s1).read().decode('utf-8')
    root = ET.fromstring(seq)

    genomic_ids = []
    mRNA_ids = []
    peptide_ids= []
    for Entrezgene_locus in root.iter('Entrezgene_locus'):
        for Gene_commentary in Entrezgene_locus.iter('Gene-commentary'):
            if Gene_commentary.find('Gene-commentary_type').get('value') == 'genomic':
                        genomic_ids.append(Gene_commentary.find('Gene-commentary_accession').text)
            if Gene_commentary.find('Gene-commentary_type').get('value') =='mRNA':
                mRNA_ids.append(Gene_commentary.find('Gene-commentary_accession').text)
            if Gene_commentary.find('Gene-commentary_type').get('value') =='peptide':
                peptide_ids.append(Gene_commentary.find('Gene-commentary_accession').text)
    return genomic_ids, mRNA_ids, peptide_ids

def main():
    gene_id = sys.argv[1]

    # fetch gene summary
    genomic_ids, mRNA_ids, peptide_ids = get_gene_summary(gene_id)

    # find 'RefSeq Selected'
    selected_id = None
    for one_id in mRNA_ids:
        if find_refseq_selected(one_id):
            selected_id = one_id

    # print fasta sequence
    if not selected_id is None:
        fetch_fasta(selected_id)


if __name__ == "__main__" :
    main()
