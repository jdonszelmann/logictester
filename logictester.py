import itertools, inspect


class logic_result:
	def __init__(self):
		self.varnames = ()
		self.cases = []

	def set_varnames(*args):
		self.varnames = args

	def add_case(inputs,result):
		self.cases.append((inputs,result))

	@property
	def truecount(self):
		count = 0
		for input,result in self.cases:
			if result:
				count+=1
		return count

	@property
	def falsecount(self):
		count = 0
		for input,result in self.cases:
			if not result:
				count+=1
		return count

	def __repr__(self):
		res = ""

		res += " ".join(func.__code__.co_varnames) + " | o\n"
		for inputs,result in self.cases:
			res += " ".join((str(i) for i in inputs)) +  " | " + str(bool(result)) + "\n"

		res += "True count: " + str(self.truecount) + "\n"
		res += "False count: " + str(self.falsecount)

def generate_combinations():
	yield from itertools.product([0, 1], repeat=func.__code__.co_argcount)

def test_logic(func):
	res = logic_result()
	res.set_varnames(*func.__code__.co_varnames)


	# print(" ".join(func.__code__.co_varnames) + " | o")
	for combination in generate_combinations():
		res.add_case(combination,func1(*combination))
		

	print("True count: ",true_counts)
	print("False count: ",false_counts)

def is_equivalent(func1,func2):
	if func1.__code__.co_argcount != func2.__code__.co_argcount:
		return ()
	
	possibilities = []
	combinations = list(itertools.product([0, 1], repeat=func1.__code__.co_argcount))
	for i in combinations:
		if func1(*i) != func2(*i):
			possibilities.append(i)

	return possibilities
	
def Implies(a,b):
	return not a or b

def And(a,b):
	return a and b

def Or(a,b):
	return a or b

def Xor(a,b):
	return a != b

def Xnor(a,b):
	return a == b

def Not(a):
	return a

def Nand(a,b):
	return not And(a,b)

def Nor(a,b):
	return not Or(a,b)



def get_expression(func):
		combinations = list(itertools.product([0, 1], repeat=func.__code__.co_argcount))

		for i in combinations:
			res = func(*i)
