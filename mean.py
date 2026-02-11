def mean(vals):
	total = 0 
	for val in vals: total += val
	return total / len(vals)



a = [3, 6, 3, 2, 5, 1, 7]

print(mean(a))