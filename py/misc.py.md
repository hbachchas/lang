```python
from matplotlib.colors import ListedColormap as lc
from matplotlib import *
import matplotlib.colors as mc
# -------------------- #
[ expression for item in list if conditional ] # list comprehension
for item in list:
    if conditional:
        expression
# -------------------- #
lambda arguments: expression
# can have any number of arguments but only one expression
# can use lambda wherever a function object is required
# -------------------- #
# need to use list encapsulation for filter, map outputs
less_than_zero = list(filter(lambda x: x < 0, range(-5, 5)))  # creates a list of elements for which a function returns true
squared = list(map(lambda x: x**2, items))  # applies a function to all the items in an input_list
from functools import reduce
product = reduce((lambda x, y: x * y), [1, 2, 3, 4]) # applies a rolling computation to sequential pairs of values in a list
```
[lambda:anonymous-functions:filter:map:reduce/](https://www.geeksforgeeks.org/python-lambda-anonymous-functions-filter-map-reduce/)  
[property decorator](https://www.programiz.com/python-programming/property)
