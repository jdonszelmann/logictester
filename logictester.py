import itertools, inspect

def logic_tester(func):
	def retfunc():
		false_counts = 0
		true_counts = 0

		combinations = list(itertools.product([0, 1], repeat=func.__code__.co_argcount))

		print(" ".join(func.__code__.co_varnames) + " | o")
		for i in combinations:
			res = func(*i)
			if res:
				true_counts+=1
			else:
				false_counts+=1

			print(" ".join((str(j) for j in i)) +  " | " + str(bool(res)))

		print("True count: ",true_counts)
		print("False count: ",false_counts)

	setattr(retfunc,"func",func)
	return retfunc

def is_equivalent(func1,func2):
	if hasattr(func1,"func"):
		func1 = func1.func

	if hasattr(func2,"func"):
		func2 = func2.func

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

