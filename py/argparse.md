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

Namespace is a simple class in module argparse
