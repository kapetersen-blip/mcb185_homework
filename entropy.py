import math

def entropy(probs):
	h = 0
	for p in probs:
		h -= p * math.log2(p)
	return h

print(entropy([0.2, 0.3, 0.5]))
