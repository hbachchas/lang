[lambda:anonymous-functions:filter:map:reduce/](https://www.geeksforgeeks.org/python-lambda-anonymous-functions-filter-map-reduce/)  
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
[property decorator](https://www.programiz.com/python-programming/property)  
```python
class Celsius:
    def __init__(self, temp = 0):
        self.t = temp

    def to_fahrenheit(self):
        return (self.t * 1.8) + 32

    @property
    def temperature(self):      # the variable and function name should be same, anything can be returned
        print("Getting value")
        return self.t           # anything can be returned

    @temperature.setter     # the setter and variable names should be same
    def temperature(self, value):       # the function and variable names should be same
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self.t = value      # anything can be set
        
c = Celsius(123)        # set the temperature with @variable.setter property
print(c.temperature)    # get the temperature with @property
c.temperature = 45      # set the temperature with @variable.setter property
print(c.temperature)    # get the temperature with @property
```
