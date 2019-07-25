'''
Coding Assignment: Elevator

 Author: Ahmed Fuad Ali
   Date: July 25, 2019
Version: 1.0.0


Summary: 

The following class models an elevator. This includes processing an array of instructions, 
displaying it's final position and actually peforming the required carloads. 


some notes:

always moves up first and then down:
    interpreted that to mean given a set of instructions with both floors going up and down
    (i.e. if we're at 4 and there's 3 and 5 both pressed)
    then we'll move to the one up first and then the one down
    (in this example, move to five first and then move to three)

won't move unless someone pushes a button



'''


class Elevator:

    # class attributes


    # initializer
    def __init__(self, floors):
        self.floors = floors

    # instance methods 
    pass


def if __name__ == "__main__":
    # let's define some test cases

    pass