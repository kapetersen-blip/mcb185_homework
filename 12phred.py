import math

def char_to_prob(char):
    if len(char) != 1:
        return None
    Q = ord(char) - 33
    if Q < 0:
        return None
    return 10 ** (-Q / 10)

def prob_to_char(prob):
    if prob < 0 or prob > 1:
        return None
    if prob == 0:
        Q = 93  # max PHRED score
    else:
        Q = int(round(-10 * math.log10(prob)))
    if Q < 0 or Q > 93:
        return None
    return chr(Q + 33)

# Test examples
print("char_to_prob('A'):", char_to_prob('A'))
print("char_to_prob('!'):", char_to_prob('!'))
print("prob_to_char(0.001):", prob_to_char(0.001))
print("prob_to_char(0):", prob_to_char(0))

