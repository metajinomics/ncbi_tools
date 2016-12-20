import xml.etree.ElementTree
import sys
file = sys.argv[1]

root = xml.etree.ElementTree.parse(file).getroot()

#print root.tag

for IPGReport in root:
    #print IPGReport.tag, IPGReport.attrib
    for RedundantGiList in IPGReport.findall('RedundantGiList'):
        for RedundantGi in RedundantGiList.findall('RedundantGi'):
            for CDSList in RedundantGi.findall('CDSList'):
                for CDS in CDSList:                    
                    print '\t'.join([CDS.get('accver'),CDS.get('start'), CDS.get('stop'), CDS.get('strand')])
