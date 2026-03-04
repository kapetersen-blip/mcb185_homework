   import sys
   import mcb185
   
for defline, seq in mcb185.read_fasta(sys.argv[1]):
     defwords = defline.split()
     name = defwords[0]
     nts = 'ACGTN'
	  counts = [0] * len(nts)
for nt in seq:
  	 idx = nts.find(nt)
     counts[idx] += 1
     print(name, end=' ')
     for n in counts: print(n/len(seq), end=' ')
print()