from logictester import *

def test1(a,b,c,d):
	return Implies(a,b and c) or (c and Xor(a,d))

def test2(a,b,c,d):
	return Implies(a,b and c) or (d and a)

def test3(a,b,c,d):
	return Implies(a,b and c) or d


print(logic(test1).find_differences(test2)) 	
print(logic(test2).find_differences(test3)) 	