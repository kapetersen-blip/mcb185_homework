1    import sys
2    import mcb185
3
4    for defline, seq in mcb185.read_fasta(sys.argv[1]):
5        defwords = defline.split()
6        name = defwords[0]
7	nts = 'ACGTN'
8   counts = [0] * len(nts)
9   for nt in seq:
10     idx = nts.find(nt)
11     counts[idx] += 1
12  print(name, end=' ')
13  for n in counts: print(n/len(seq), end=' ')
14  print()