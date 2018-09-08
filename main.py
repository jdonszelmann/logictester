from logictester import *

def test1(a,b,c,d):
	return Implies(a,b and c) or (c and Xor(a,d))

def test2(a,b,c,d):
	return Implies(a,b and c) or (d and a)

def test3(a,b,c,d):
	return Implies(a,b and c) or d

print(is_equivalent(test1,test2))
print(is_equivalent(test2,test3))