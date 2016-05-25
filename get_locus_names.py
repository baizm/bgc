import re

f='/scratch/lsa_flux/baizm/snpCalling/filtered_final.vcf' 
o='/scratch/lsa_flux/baizm/bgc/loci.csv' 

f=open(f, 'r')
o=open(o, 'w')

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
