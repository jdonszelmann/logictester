
from logictester import *

def test1(a,b,c,d):
	return Implies(a,b and c) or (c and Xor(a,d))

print(test_logic(test1))