# instance Methods :
#   normal methods in the class
#   automatically take the instance reference "self"

# class Methods :
#   like static methods
#   automatically take the class reference as first variable
#   @classmethod decorator is used to define a class method

# by convention, a class method should be called on a class name not on instance name; although both work same

class Birds:
    birdtype = 'default class name'

    def __init__(self,name='',legs='',tailSize=''):
        self.birdtype = name
        self.legs = legs
        self.tailSize = tailSize

    @classmethod
    def setDefaultBirdClassName(cls, newbirdtype):
        cls.birdtype = newbirdtype
        # Birds.birdtype = newbirdtype      # both work same

    @classmethod
    def from_string(cls, bird_str):                     # an Alternative constructor
        name, legs, tailSize = bird_str.split('-')
        return cls(name,legs,tailSize)

def genericExample():
    bird1 = Birds()
    print(Birds.birdtype)
    bird1.setDefaultBirdClassName('dcn1')   # will pass class ref even when called on instance # doesn't make a lot of sense
    bird2 = Birds()
    print(bird2.birdtype, Birds.birdtype)
    Birds.setDefaultBirdClassName('dcn2')   # will pass class ref when called on class
    print(Birds.birdtype)

def classMethodAsAlternativeConstructors():
    bird1 = Birds.from_string('hen-2-short')    # example of Alternative constructor
    print(bird1.birdtype, bird1.legs, bird1.tailSize)
    bird2 = Birds()
    print(bird2.birdtype, bird2.legs, bird2.tailSize)   # using default values

if __name__ == "__main__":
    # genericExample()
    classMethodAsAlternativeConstructors()