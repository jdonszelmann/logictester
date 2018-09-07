
from logictester import *

@logic_tester
def test1(a,b,c,d):
	return Implies(a,b and c) or (c and Xor(a,d))

test1()