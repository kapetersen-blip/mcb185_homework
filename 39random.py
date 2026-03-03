import random
import sys

def random_subseq(seq, n, k):
	subs = []
	for _ in range(n):
		x = random.randint(0, len(seq) -k)
		subseq = seq[x:x+k]
		subs.append(subseq)
		
	return subs
	
	
	
seq = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
subseqs = random_subseq(seq, 5, 3)
print(subseqs)