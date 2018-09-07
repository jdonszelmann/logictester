
from logictester import *


@logic_tester
def test1(p,q,r):
	return (p and q) and r

@logic_tester
def test2(p,q,r):
	return p and (q and r)


test1()
test2()
