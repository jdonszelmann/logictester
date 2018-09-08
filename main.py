from logictester import *

def test1(a,b,c,d):
	return Implies(a,b and c) or d


print(logic(test1).find_expression())
#prints (a) v (¬a ^ ¬d) v (¬a ^ ¬b ^ ¬c ^ d)