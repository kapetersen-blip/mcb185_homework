import math

def entropy(probs):
    if not math.isclose(sum(probs), 1.0, rel_tol=1e-9):
        raise ValueError("Probabilities must sum to 1.")
    
    h = 0
    for p in probs:
        if p > 0:  # avoid log2(0)
            h -= p * math.log2(p)
    
    return h


print(entropy([0.2, 0.3, 0.5]))
