```python
class C(object):
    pass
c=C()

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--foo')
args = parser.parse_args(['--foo', 'BAR'], namespace=c)
print(args)
print(vars(args))
print(type(args))


c.st = 'c string'
print(type(c))
print(c.st)
print(vars(c))
```

* Namespace is a simple class in module argparse
* any other class can also take its place such as in above code the class C
* vars converts the object/class/variables etc. into a dictonary
