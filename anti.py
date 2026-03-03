import sys

def anti(nt):
	nt = nt.upper()
	
	complement = {
		'A': 'T',
		'T': 'A',
		'G': 'C',
		'C': 'G'
	}
	
	rev_comp = " "
	
	for base in reversed(nt):
		rev_comp += complement[base]
		
	return rev_comp
	
if len(sys.argv) < 2:
	print("Usage: python3 anti.py <DNA sequence>")
	sys.exit()

dna_sequence = sys.argv[1]

print(anti(dna_sequence))