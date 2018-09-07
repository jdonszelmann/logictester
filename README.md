
# Logic Tester

this little library can test your logic expressions.

to write a testable logic expression, one can use the following replacements for the default binary connectives:

| python | bianry connective | 
| --- | --- |
| not	(Not(a,b))	| 		¬				|
| and	(And(a,b))	| 		^				|
| or 	(Or(a,b))	| 		v 				|
| Xor(a,b)			| 		⊕ 				|
| Xnor(a,b)			| 		⇔				|
| Implies(a,b)		| 		->				|

To start testing a logical expression, one writes a function like this, with as many parameters as will be used in the expression (This is important):

```python
from logictester import *


def test1(a,b,c,d):
	return Implies(a,b and c) or (c and Xor(a,d))

```

it's important that the result of this expression will be returned. within the function you wrote you can do anything as long as the return value is a boolean. In most cases a one-line function as above will suffice.

now comes the magic:

to generate a truth table of this expression, first put the following on the line before the function:
```python
@logic_tester
```

so you get:
 
```python
from logictester import *

@logic_tester
def test1(a,b,c,d):
	return Implies(a,b and c) or (c and Xor(a,d))

```

now when you call this function 
```python
test1()
```

the truth table of this function will be printed.

the ammount of arguments to the logic_tester is arbitrary. it will automatically be determined. This doesn't mean any number of arguments is possible. this is due to the fact that the algorithm used is O(2^n) which is *SLOW*. so to not-overflow your terminal and keep execution time reasonable, be reasonable with the ammount of arguments.

---

One can also test for equivalence of two functions with logictester. this can be done as follows: (the`@logic_tester` is optional)

```python

@logic_tester
def test1(a,b,c,d):
	return Implies(a,b and c) or (c and Xor(a,d))

@logic_tester
def test2(a,b,c,d):
	return Implies(a,b and c) or (d and a)

@logic_tester
def test3(a,b,c,d):
	return Implies(a,b and c) or d


print(is_equivalent(test1,test2)) 	
#will return [(1, 0, 0, 1), (1, 0, 1, 0), (1, 0, 1, 1), (1, 1, 0, 1)] 
#since these are the input cases in which test1 and test2 differ

print(is_equivalent(test1,test3))
#will return an empty list (`[]`) to signify the two are equivalent
```


