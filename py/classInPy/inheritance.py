
class Birds(object):        # for using super(), need to explicitly inherit object
    birdtype = 'default class name'
    def __init__(self,name='',legs='',tailSize=''):
        self.birdtype = name
        self.legs = legs
        self.tailSize = tailSize
    @staticmethod
    def can_fly():      # true for all birds
        print('yes')

class Raptors(Birds):   
    flying_speed = 'very fast'
    def __init__(self,name='',legs='',tailSize='',clawSize=''):
        # super(self.__class__,self).__init__(name, legs, tailSize)          # call the parent class constructor
        Birds.__init__(self, name, legs, tailSize)      # both ways can be used to call parent class constructor; this works best
        self.clawSize = clawSize

if __name__ == "__main__":
    bird1 = Birds()
    raptor1 = Raptors()
    print( raptor1.can_fly(), raptor1.flying_speed )
    print( raptor1.__dict__ )

    # print(help(raptor1))        # shows class construction details