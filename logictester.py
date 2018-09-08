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

	def __eq__(self,other):
		return self.find_differences(other) == []

	def __repr__(self):
		res = ""

		res += " ".join(self.varnames) + " | o\n"
		for inputs,result in self.cases:
			res += " ".join((str(i) for i in inputs)) +  " | " + str(bool(result)) + "\n"

		res += "True count: " + str(self.truecount) + "\n"
		res += "False count: " + str(self.falsecount)
		return res


	def find_expression(self):
		def inverse_of_part(part):
			for i in part:
				if "¬" in i:
					yield i.replace("¬","")
				else:
					yield "¬" + i

		def sameatom(x,y):
			if x.startswith("¬"):
				x = x[1:]
			if y.startswith("¬"):
				y = y[1:]
			return x == y

		def differences(part1,part2):
			if len(part1) != len(part2):
				return []
			res = []
			index = 0
			for x,y in zip(part1,part2):
				if x != y and sameatom(x,y):
					res.append(index)
				index+=1
			return res

		class FoundError(Exception):
			pass

		class FoundAllError(Exception):
			pass

		#generate parts
		parts = []
		for inputs,result in self:
			if result:
				atoms = []
				for index,i in enumerate(inputs):
					if i:
						atoms.append("¬" + self.varnames[index])
					else:
						atoms.append(self.varnames[index])
				parts.append(atoms)


		# #remove inverses
		# for i in parts:
		# 	inv = list(inverse_of_part(i))
		# 	if inv in parts:
		# 		parts.remove(i)
		# 		parts.remove(inv)

		# print(" v ".join("({})".format(" ^ ".join(i)) for i in parts))
		
		#simplify near-misses
		try:
			while True:
				try:
					for index1,i in enumerate(parts):
						for index2,j in enumerate(parts):
							d = differences(i,j)
							if len(d) == 1:
								del parts[index1][d[0]]
								del parts[index2][d[0]]
								raise FoundError
					raise FoundAllError
				except FoundError:
					pass
		except FoundAllError:
			pass

		# print(" v ".join("({})".format(" ^ ".join(i)) for i in parts))

		# #remove inverses again
		# for i in parts:
		# 	inv = list(inverse_of_part(i))
		# 	if inv in parts:
		# 		parts.remove(i)
		# 		parts.remove(inv)

		oldparts = parts
		parts = []
		
		#remove duplicates
		for i in oldparts:
			if i not in parts:
				parts.append(i)

		#display nice
		return " v ".join("({})".format(" ^ ".join(i)) for i in parts)

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



