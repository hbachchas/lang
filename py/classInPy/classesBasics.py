# when a call to the object creation is made
# first all the propoerties are inherited as-is
# then the __init__() method is executed and whatever is inside it gets executed
# so if the __init__() method contains some propoerty initialization code then it gets executed


# self : reference to the instance; it can be named anything other than 'self'

# instance variable :
#   contain data unique to each instance
#   each instance can contain any number of variables (need not be same)
#   new variables can be created after instantiating the object

# class variable :
#   shared amongst all instance variables of the class
#   accessed : through either class name, or instance name (if no instance variable with same name is declared)

class Animals:
    animaltype = 'default class name'
    num_of_animals = 0

    def __init__(self, name='default instance name'):
        self.animaltype = name      # this creates and assigns value to the instance variable
        Animals.num_of_animals += 1

    def getNumberOfLegs(self):
        if self.animaltype == 'elephant':
            return 4
        elif self.animaltype == 'lion':
            return 4

def genericExamples():
    elephant = Animals('elephant')
    lion = Animals('lion')
    print(Animals.num_of_animals)

    #-------------- USING METHODS --------------
    # print(elephant.animaltype)
    # print(lion.animaltype, lion.getNumberOfLegs())      # lion.getNumberOfLegs() is transformed into Animals.getNumberOfLegs(lion) and then gets executed
    # print( Animals.getNumberOfLegs(lion) )              # we do need to pass the instance

    #-------------- DELETE INSTANCE --------------
    # del lion
    
    #-------------- instance variable: contain data for that instance only --------------
    # ani1 = Animals()
    # ani1.legs = 4
    # ani1.tailSize = 'short'
    # print(ani1.animaltype, ani1.legs, ani1.tailSize)

    #-------------- difference between class variables and instance variables --------------
    print(elephant.animaltype)
    del elephant.animaltype     # will delete the instance variable
    # del elephant.animaltype     # will throw error because there is no more instance variable to be deleted
    print(elephant.animaltype)

if __name__ == "__main__":
    genericExamples()
