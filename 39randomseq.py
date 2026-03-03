import random 

def random_subseq(seq, n, k):
	samples = []
	for i in range(n): 
		x = random.randint(0, len(seq) - k)
		subseq = seq[x:x + k]
		samples.append(subseq)
	return samples



dna = 'ABJAHSNLLKIANDNS'
sequences = random_subseq(dna, 5, 3)
print(sequences)