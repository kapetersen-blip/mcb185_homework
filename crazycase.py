import sys

def crazy_case(text):
	result = ""
	make_upper = True
	
	for char in text:
		if char.isalpha():
			if make_upper:
				result += char.upper()
			else:
				result += char.lower()
			make_upper = not make_upper
		else:
			result += char
			
	return result
	
	
filename = sys.argv[1]

with open(filename, 'r') as file:
		content = file.read()
		
converted = crazy_case(content)

print(converted)