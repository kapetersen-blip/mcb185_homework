def minmax(vals):
	mymin = vals[0]
	mymax = vals[0]
	for val in vals[1:]:
		if val > mymax: mymax = val
		if val < mymin: mymin = val
	return mymin, mymax	
	
	
a = [5, 7, 3, 8, 2, 1, 23, 56]
print(minmax(a))
