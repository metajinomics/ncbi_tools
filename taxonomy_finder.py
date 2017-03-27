#!/usr/bin/python
# this module return full taxonomy lineage. Cannot handle multiple genbank info in one file. should be one genbank id in each file

#import urllib
#import cStringIO
#import pycurl

import urllib2


def get_taxonomy(tax_id):
    #flist = [locus,taxon]
    
    flist = []
    #buf = cStringIO.StringIO()
    #c = pycurl.Curl()
    #c.setopt(c.URL, 'https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?mode=Info&id=' + taxon)
    #c.setopt(c.WRITEFUNCTION, buf.write)
    #c.perform()

    #x= buf.getvalue()
    #dat = x.split('\n')

    url_template = "https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?mode=Info&id=%s"
    ge = urllib2.urlopen(url_template % tax_id).read()
    #dat= ge.split('\n')

    #print dat
    #for line in dat:
    #    if('<dd><a ALT' in line):
    taxID=""
    line = ge
    lenID = len(taxID)
    lenCut = 163+lenID
    
    Kt = ""
    Pt = ""
    Ct = ""
    Ot = ""
    Ft = ""
    Gt = ""
    St = ""

    startK = line.find("TITLE=\"superkingdom\">")
    if startK > 0:
        startK = startK + 21
        endK = line.find("</a", startK) 
    #print startK, endK
    
        if (endK == lenCut):
            Kt = "null"
            flist.append("null")
        else:
            Kt = line[startK:endK]
            flist.append(line[startK:endK])
    else:
        Kt = "null"

    startP = line.find("TITLE=\"phylum\">")
    if startP > 0:
        startP = startP + 15
        endP = line.find("</a", startP) 
        if (endP == lenCut):
            Pt = "null"
            flist.append("null")
        else:
            Pt = line[startP:endP]
            flist.append(line[startP:endP])
    else:
        Pt = "null"

    startC = line.find("TITLE=\"class\">")
    if startC > 0:
        startC = startC + 14
        endC = line.find("</a", startC)
        if (endC == lenCut):
            Ct = "null"
            flist.append("null")
        else:
            Ct = line[startC:endC]
            flist.append(line[startC:endC])
    else:
        Ct = "null"
    
    startO = line.find("TITLE=\"order\">")
    if startO > 0:
        startO = startO + 14
        endO = line.find("</a", startO)
        if (endO == lenCut):
            Ot = "null"
            flist.append("null")
        else:
            Ot = line[startO:endO]
            flist.append(line[startO:endO])
    else:
        Ot = "null"

    startF = line.find("TITLE=\"family\">")
    if startF > 0:
        startF = startF + 15
        endF = line.find("</a", startF)
        if (endF == lenCut):
            Ft = "null"
            flist.append("null")
        else:
            Ft = line[startF:endF]
            flist.append(line[startF:endF])
    else:
        startF = "null"

    startG = line.find("TITLE=\"genus\">")
    if startG > 0:
        startG = startG + 14
        endG = line.find("</a", startG)
        if (endG == lenCut):
            Gt = "null"
            flist.append("null")
        else:
            Gt = line[startG:endG]
            flist.append(line[startG:endG])
    else:
        Gt = "null"

    startS = line.find("TITLE=\"species\">")
    if startS > 0 :
        startS = startS + 16
        endS = line.find("</a", startS)
        if (endS == lenCut):
            St = "null"
            flist.append("null")
        else:
            St = line[startS:endS]
            flist.append(line[startS:endS])
    else:
        startS = line.find("Taxonomy browser")
        startS = startS + 18
        endS = line.find(")</title>", startS)
        #print startS,endS
        St = line[startS:endS]
        flist.append(line[startS:endS])
    flist = [Kt,Pt,Ct,Ot,Ft,Gt,St]
    #print flist
    return flist

def full(filename):
    fread = open(filename,'r')
    locus = ""
    taxon = ""
    flag = 0
    plasmid = 0
    full_tax = ""
    for gbline in fread:
        if ("LOCUS" in gbline):
            locus = gbline.strip().split(" ")[7]
        if ("DEFINITION" in gbline):
            if("plasmid" in gbline):
                   plasmid = 1
        if ("taxon:" in gbline) and flag == 0:
            taxon = gbline.strip().split(":")[1][:-1]
            flag = 1
        if (gbline.strip()[:2] == "//" and plasmid == 0):
            flist = get_taxonomy(locus,taxon)
            #full_tax = ""
            for item in flist:
                full_tax = full_tax + item+'\t'
            #print full_tax
            flag = 0
            return full_tax
        elif (gbline.strip()[:2] == "//" and plasmid == 1):
            plasmid = 0

    return full_tax
    
def from_id(taxid):
    full_tax = ""
    locus = ""
    taxon = taxid
    flist = get_taxonomy(locus,taxon)
    for item in flist:
        full_tax = full_tax + item+'\t'
    return full_tax
