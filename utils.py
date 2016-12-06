import gzip
from string import maketrans

def get_rc(seq):
    seq = seq.upper()
    trans = maketrans("AGCT","TCGA")
    seq = seq.translate(trans,'xm')
    seq = seq[::-1]
    return seq

def get_from_url(seq):
    spl = seq.split('\n')
    if(len(spl)>1):
        spl[1]= get_rc(spl[1])
    seq = '\n'.join(spl)
    return seq



def read_map(filename):
    dict={}
    for line in open(filename,'r'):
        spl = line.strip().split('\t')
        dict[spl[1]] = spl[0]
    return dict

def read_check_match(filename):
    dict ={}
    name = ''
    for line in open(filename,'r'):
        if('.txt' in line):
            name = line.strip()
        else:
            if (dict.has_key(name)):
                temp = dict[name]
                temp.append(line.strip())
                dict[name] = temp
            else:
                dict[name] = [line.strip()]
    return dict

def get_target_seq(locus,filename):
    flag = 0
    seq = ""
    for line in open(filename,'r'):
        if(line[:1] == ">"):
            spl = line.split(' ')
            if (locus == spl[0][1:]):
                flag = 1
        elif(line[:1] != ">" and flag == 1):
            seq = line.strip()
            return seq
            flag = 0
    return seq



def if_amplified(fpri,rpri,seq):
    target = False
    if(fpri in seq and rpri in seq):
        target = True
    return target

def read_arg_list(filename):
    li = []
    for line in open(filename,'r'):
        spl = line.strip().split('\t')
        if(len(spl)==3):
            li.append([spl[0],spl[1].split(':')[0],spl[2].split(':')[0]])
    return li

def read_arg_list_all(filename):
    li = []
    for line in open(filename,'r'):
        spl = line.strip().split('\t')
        if(len(spl)==3):
            li.append([spl[0],spl[1].split(':')[0],spl[2].split(':')[0]])
        else:
            li.append([spl[0],spl[1].split(':')[0]])
    return li

def read_final_list(filename):
    li = []
    for n, line in enumerate(open(filename,'r')):
        if(n == 0):
            continue
        spl = line.strip().split('\t')
        temp = []
        for x in spl:
            temp.append(x)
        li.append(temp)
    return li

def check_error(filename):
    outread = open(filename,'r')
    print filename
    flag = 0
    for line in outread:
        if("ERROR" in line):
            print "error: "+line
            flag = 1
        elif("PROBLEMS" in line):
            print "problem: "+line
            flag = 1
    if (flag == 0):
        print "no problem"

def read_fasta(filename):
    fread = open(filename,'r')
    dict = {} 
    name = ""
    flag = 0
    for line in fread:
        if(line[:1] == ">"):
            name = line.strip()
        else:
            if(dict.has_key(name)):
                temp = dict[name]
                temp = temp + line.strip()
                dict[name] = temp
            else:
                dict[name] = line.strip()
    return dict
    
def read_fasta_refseq(filename):
    if filename[-2:] == 'gz':
        fread = gzip.open(filename,'rb')
    else:
        fread = open(filename,'r')

    dict = {} 
    name = ""
    flag = 0
    for line in fread:
        if(line[:1] == ">"):
            name = line.strip().split('|')[3].split('.')[0]
        else:
            if(dict.has_key(name)):
                temp = dict[name]
                temp = temp + line.strip()
                dict[name] = temp
            else:
                dict[name] = line.strip()
    return dict

def read_fasta_usda(filename):
    fread = open(filename,'r')
    dict = {}
    name = ""
    flag = 0
    for line in fread:
        if(line[:1] == ">"):
            name = line.strip().split(' ')[0][1:]
        else:
            if(dict.has_key(name)):
                temp = dict[name]
                temp = temp + line.strip()
                dict[name] = temp
            else:
                dict[name] = line.strip()
    return dict

