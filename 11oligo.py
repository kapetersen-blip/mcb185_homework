# oligo melting temperature calculator

def tm(A, C, G, T):
    """
    Compute melting temperature of an oligo.
    
    Parameters:
    A, C, G, T : int
        Number of A, C, G, T nucleotides in the oligo
        
    Returns:
    float
        Melting temperature in degrees Celsius
    """
    length = A + C + G + T
    if length <= 13:
        # short oligos formula
        return (A + T) * 2 + (G + C) * 4
    else:
        # longer oligos formula
        return 64.9 + 41 * (G + C - 16.4) / length

print("Short oligo Tm:", tm(5, 3, 3, 2))   # example <= 13 nt
print("Long oligo Tm:", tm(20, 15, 25, 10))  # example > 13 nt
print("Another short oligo Tm:", tm(3, 4, 3, 3))
print("Another long oligo Tm:", tm(30, 25, 25, 20))

