import re
import gzip
import sys

in_file = sys.argv[1]
out_file = sys.argv[2]

f=gzip.open(in_file, 'r')
o=open(out_file, 'w')

n_loci=-1

for i in f:
	if '#' not in i:
		split=re.split('\t', i.strip())
		n_loci += 1
		l=' '.join(map(str,split[0:2]))
		o.write('loc_'+str(n_loci)+' '+l+'\n')

#to make file with bgc locus numbers & names corresponding from vcf file
#e.g.:
#loc_0 flattened_line_0 1234
#use grep w/outliers ID file from R to associate locus index with contig/position:
#grep -wf beta_outliers_id.txt loci.txt > beta_outliers_contigs.txt
