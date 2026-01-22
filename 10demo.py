# 10demo.py by Katelyn Petersen

import math

print('hello, again')
print(1.5e-2)
print(1 + 1)
print(2**3)
print(pow(2, 3))
print(math.pow(2, 3))
print(2**0.5)
print(math.sqrt(2))
print(math.log(2))
#print(1 / 0)           # divide by zero error
#print(math.log(0))     # math domain error
#print(math.sqrt(-1))   # math domain error
def pythagoras(a, b):
	c = math.sqrt(a**2 + b**2)
	return c
hyp = pythagoras(3, 4)
print(hyp)               
import math

# Circle area
def circle_area(r):
    return math.pi * r**2

# Rectangle area
def rectangle_area(w, h):
    return w * h

# Triangle area using rectangle_area
def triangle_area(w, h):
    return rectangle_area(w, h) / 2

# Circle circumference
def circle_circumference(r):
    return 2 * math.pi * r

# Fahrenheit to Celsius
def f_to_c(f):
    return (f - 32) * 5 / 9

# Celsius to Fahrenheit
def c_to_f(c):
    return c * 9 / 5 + 32

# MPH to KPH
def mph_to_kph(mph):
    return mph * 1.60934

# KPH to MPH
def kph_to_mph(kph):
    return kph / 1.60934

# Compute DNA concentration from OD260
# Assume standard: 1 OD260 unit = 50 ug/mL for dsDNA
def dna_concentration(od260):
    return od260 * 50

# Arithmetic mean of 3 numbers
def arithmetic_mean(a, b, c):
    return (a + b + c) / 3

# Geometric mean of 3 numbers
def geometric_mean(a, b, c):
    return (a * b * c) ** (1/3)

# Harmonic mean of 3 numbers
def harmonic_mean(a, b, c):
    return 3 / (1/a + 1/b + 1/c)

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print("Circle area r=2:", circle_area(2))
print("Triangle area 3x4:", triangle_area(3,4))
print("100 F in C:", f_to_c(100))
print("Distance between (0,0) and (3,4):", distance(0,0,3,4))

s = 'hello world'
print(s, type(s))

a = 2
b = 2
if a == b:
	print('a equals b')
print (a, b)

def is_even(x):
	if x % 2 == 0: return True
	return False

print(is_even(2))
print(is_even(3))

c = a == b
print(c)
print(type(c))

if a < b:
	print('a < b')
elif a > b:
	print('a > b')
else:
	print('a == b')
if   a < b: print('a < b')
elif a > b: print('a > b')
else:       print('a == b')

if   a < b:  print('a < b')
elif a <= b: print('a <= b')
elif a == b: print('this will never print!')
