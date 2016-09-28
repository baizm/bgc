import sys
from Bio import SeqIO

fasta = open(sys.argv[1], 'rU')
wanted_file = sys.argv[2]
out_file = sys.argv[3]

o=open(out_file, 'w')

#create a set of target contigs for length calculation from file of target contigs
wanted = set()
with open(wanted_file) as f:
        for line in f:
                line = line.strip()
                if line != "":
                        wanted.add(line)

for i in SeqIO.parse(fasta, 'fasta'):
    name = i.id
    seqLen = len(i)
    if i.id in wanted:
            o.write(str(name)+"\t"+str(seqLen)+"\n")

fasta.close()

#usage get_seqLength.py	fasta.fa wanted.txt out.txt
#on flux, must load modules python-anaconda2/201607 biopython/1.60
