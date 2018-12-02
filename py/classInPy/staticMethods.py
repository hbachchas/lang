# static methods :
#   don't pass anything automatically i.e. neither instance reference nor class reference
#   behave like regular functions, but are put inside class as they have some logical connection with the class

class Birds:
    birdtype = 'default class name'

    def __init__(self,name='',legs='',tailSize=''):
        self.birdtype = name
        self.legs = legs
        self.tailSize = tailSize

    @staticmethod
    def can_fly():      # true for all birds
        print('yes')

if __name__ == "__main__":
    bird1 = Birds()
    bird1.can_fly()     # both instance, class can call static method
    Birds.can_fly()