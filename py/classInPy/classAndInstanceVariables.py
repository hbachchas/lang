
# instance variable :
#   contain data unique to each instance
#   each instance can contain any number of variables (need not be same)
#   new variables can be created after instantiating the object

# class variable :
#   shared amongst all instance variables of the class
#   accessed : through either class name, or instance name (if no instance variable with same name is declared)

# variable checking: first the variable is looked inside the instance, if not present there then it is looked in the class

class Birds:
    birdtype = 'default class name'
    def __init__(self):
        print(birdtype, self.birdtype, Birds.birdtype)      # first variable is global scope, second and third are class variable

    def getBirdName(self):
        self.birdtype = 'default instance name'
        print(birdtype, self.birdtype, Birds.birdtype)      # first variable is global scope, second is instance variable, third is class variable

birdtype = 'random bird'

def exampleOfVariables():
    bird1 = Birds()
    print(birdtype, bird1.birdtype)     # first variable is global scope, second is class variable, since it doesn't point to an instance variable
    print(bird1.getBirdName())
    print(birdtype, bird1.birdtype)     # first variable is global scope, second is instance variable, since it points to an instance variable

def checkNamespace():
    bird1 = Birds()
    print(bird1.__dict__)       # access the Instance namespace using __dict__
    print(Birds.__dict__)       # access the Class namespace using __dict__

def createNewInstanceVars():
    bird1 = Birds()
    bird1.legs = 2       # new variables for an instance can be created on the fly
    bird1.tailSize = 'short'
    print(bird1.birdtype, bird1.legs, bird1.tailSize)

if __name__ == "__main__":
    # exampleOfVariables()
    # checkNamespace()
    createNewInstanceVars()

