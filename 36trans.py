import sys
import itertools 
def translate(orf):
	codons = [''.join(t) for t in itertools.product('ACGT', repeat=3)] 
	trans = 'KNKNTTTTRSRSIIMIQHQHPPPPRRRRLLLLEDEDAAAAGGGGVVVV*Y*YSSSS*C CLFLF'
	prot = ''
	for i in range(0, len(orf), 3):
		codon = orf[i:i+3]
		idx = codons.index(codon)
		aa = trans[idx]
		prot += aa
	
	return prot
	
protein = translate ('ATAGCGAAT')
print(protein)