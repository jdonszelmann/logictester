import itertools, inspect


class logic:
	def __init__(self,func):
		self.varnames = ()
		self.cases = []

		self.set_varnames(*func.__code__.co_varnames)

		for combination in generate_combinations(func.__code__.co_argcount):
			self.add_case(combination,func(*combination))

	def set_varnames(self,*args):
		self.varnames = args

	def add_case(self,inputs,result):
		self.cases.append((inputs,result))

	@property
	def truecount(self):
		count = 0
		for inputs,result in self.cases:
			if result:
				count+=1
		return count

	@property
	def falsecount(self):
		count = 0
		for inputs,result in self.cases:
			if not result:
				count+=1
		return count

	def __iter__(self):
		for inputs,result in self.cases:
			yield inputs,result

	def find_differences(self,other):
		if type(other) != self.__class__:
			other = self.__class__(other)

		differences = []

		for a,b in zip(self,other):
			inputs1,result1 = a
			inputs2,result2 = b

			if result1 != result2:
				differences.append(inputs1)

		return differences

	def __repr__(self):
		res = ""

		res += " ".join(self.varnames) + " | o\n"
		for inputs,result in self.cases:
			res += " ".join((str(i) for i in inputs)) +  " | " + str(bool(result)) + "\n"

		res += "True count: " + str(self.truecount) + "\n"
		res += "False count: " + str(self.falsecount)
		return res


def generate_combinations(n):
	yield from itertools.product([0, 1], repeat=n)

def is_equivalent(func1,func2):
	return logic(func1).find_differences(func2) == []

	
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
