def gc_comp(dna):
	dna = dna.upper()
	g_count = dna.count('G')
	c_count = dna.count('C')
	total = len(dna)
	
	if total == 0:
		return 0
		
	gc_content = (g_count + c_count) / total
	return gc_content 
	
sequence = input("Enter a DNA Sequence: ")

gc = gc_comp(sequence)

print("GC composition:", gc)