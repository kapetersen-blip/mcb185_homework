def mini(vals):
	mini = vals[0]
	for val in vals[1:]:
		if val < mini: mini = val
	return mini
	
vals = [3, 4, 7, 56, 23, 12, 6, 8, 2]

print(mini(vals))