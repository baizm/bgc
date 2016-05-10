import re

out_dir = '/scratch/lsa_flux/baizm/bgc/'

#for a single admixed population
f='%shz_filtered.recode.vcf' % (out_dir)
o='%sbgc_hz_filtered.txt' % (out_dir)

f=open(f, 'r')
o=open(o, 'w')

n_loci=0

for i in f:
	if '#' not in i:
		n_loci += 1
		o.write('locus '+str(n_loci)+'\npop 0\n')
		split=re.split('\t', i.strip())
		t=split[9:]
		for i in t:
			GT,PL,DP,DPR=i.split(':')
			o.write(DPR.replace(',',' ')+'\n')
			
f.close()
o.close()

#for parental pop 1
f='%sapi_filtered.recode.vcf' % (out_dir)
o='%sbgc_api_filtered.txt' % (out_dir)

f=open(f, 'r')
o=open(o, 'w')

n_loci=0

for i in f:
	if '#' not in i:
		n_loci += 1
		o.write('locus '+str(n_loci)+'\n')
		split=re.split('\t', i.strip())
		t=split[9:]
		for i in t:
			GT,PL,DP,DPR=i.split(':')
			o.write(DPR.replace(',',' ')+'\n')
			
f.close()
o.close()

#for parental pop 2
f='%sapm_filtered.recode.vcf' % (out_dir)
o='%sbgc_apm_filtered.txt' % (out_dir)

f=open(f, 'r')
o=open(o, 'w')

n_loci=0

for i in f:
	if '#' not in i:
		n_loci += 1
		o.write('locus '+str(n_loci)+'\n')
		split=re.split('\t', i.strip())
		t=split[9:]
		for i in t:
			GT,PL,DP,DPR=i.split(':')
			o.write(DPR.replace(',',' ')+'\n')
			
f.close()
o.close()
