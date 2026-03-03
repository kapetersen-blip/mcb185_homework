import sys
def oligo_tm(dna):
	dna = dna.upper()
	
	a = dna.count('A')
	t = dna.count('T')
	g = dna.count('G')
	c = dna.count('C')
	
	length = a + t + g + c
	
	if length <= 13:
		tm = (a + t) * 2 + (g + c) * 4
	else:
		tm = 64.9 + 41 * (g + c - 16.4) / length
	return tm
	
dna_sequence = sys.argv[1]

tm_value = oligo_tm(dna_sequence)


print("Melting temperature (Tm):", tm_value)
