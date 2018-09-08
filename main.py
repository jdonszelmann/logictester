from logictester import *

def test1(a,b,c,d):
	return Implies(a,b and c) or (c and Xor(a,d))

def test2(a,b,c,d):
	return Implies(a,b and c) or (d and a)

def test3(a,b,c,d):
	return Implies(a,b and c) or d

def test4(a,b,c,d):
	return a or (not a and (not d)) or ((not a) and (not b) and (not c) and d) 

# (a) v (¬a ^ ¬d) v (¬a ^ ¬b ^ ¬c ^ d)

print(logic(test3).find_expression())

print(logic(test3))
print(logic(test4))