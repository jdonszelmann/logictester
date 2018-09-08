
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

to generate a truth table of this expression, call the logic function with as the first and only argument the function:
```python
test_logic(test1)
```

so you get:
 
```python
from logictester import *

def test1(a,b,c,d):
	return Implies(a,b and c) or (c and Xor(a,d))


print(logic(test1))
```

the truth table of this function will be printed like this:    
a b c d | o  
0 0 0 0 | True  
0 0 0 1 | True  
0 0 1 0 | True  
0 0 1 1 | True  
0 1 0 0 | True  
0 1 0 1 | True  
0 1 1 0 | True  
0 1 1 1 | True  
1 0 0 0 | False  
1 0 0 1 | False  
1 0 1 0 | True  
1 0 1 1 | False  
1 1 0 0 | False  
1 1 0 1 | False  
1 1 1 0 | True  
1 1 1 1 | True  
True count:  11  
False count:  5  

the ammount of arguments to the logic_tester is arbitrary. it will automatically be determined. This doesn't mean any number of arguments is possible. this is due to the fact that the algorithm used is O(2^n) which is *SLOW*. so to not-overflow your terminal and keep execution time reasonable, be reasonable with the ammount of arguments.

---

One can also test for equivalence of two functions with logictester. this can be done as follows: 

```python

from logictester import *

def test1(a,b,c,d):
	return Implies(a,b and c) or (c and Xor(a,d))

def test2(a,b,c,d):
	return Implies(a,b and c) or (d and a)

def test3(a,b,c,d):
	return Implies(a,b and c) or d


print(is_equivalent(test1,test2)) 	
#will return False
#since these are the input cases in which test1 and test2 differ

print(is_equivalent(test1,test3))
#will return True
```


