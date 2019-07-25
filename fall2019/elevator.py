'''
Coding Assignment: Elevator

 Author: Ahmed Fuad Ali
   Date: July 25, 2019
Version: 1.0.0


Summary: 

The following class models an elevator. This includes processing an array of instructions, 
displaying it's final position and actually peforming the required carloads. 


some Ambiguities:

always moves up first and then down:
    interpreted that to mean given a set of instructions with both floors going up and down
    (i.e. if we're at 4 and there's 3 and 5 both pressed)
    then we'll move to the one up first and then the one down
    (in this example, move to five first and then move to three)

No total floor count given for the building:
    because this wasn't specified, I assumed a building of 30 floors, 
    and in each of my methods I added the # of floors serviced to 
    be a constraint of the problem. this can be customized by the user

Assumptions
    I didn't take into account certain edge cases, given the practical nature of the problem.
    Some examples: I didn't account for negative values in my arrays, since I assummed 
    that there would only be floors above ground. This can be implemented pretty easily. 

    when letting people out of the elevator, no one comes in at that floor. otherwise, the 
    set of input carloads would change, and we would have to account for that. 



'''


class Elevator:

    # initializer
    def __init__(self, floors, start):
        self.floors = floors
        self.start = start

    # instance methods
    def process_floors(self, arr):
        # takes in an array of arrays of carloads, outputs 
        # how many stops, carloads processed, floors it passed, final floor
        
        # initialize outputs
        total_carloads = len(arr)
        total_stops = 0
        floors_passed = 0

        # keep track of what floor we're at 
        position = self.start 

        # remove duplicates in carload and sort them from least to greatest 
        arr = list(map(lambda x: sorted(list(set(x))), arr))

        print("Array after sorting and removing duplicates: ", arr)

        # now, for each carload, determine movements
        for i in arr:
            floors_below = []
            total_stops += len(i)

            # traverse floors above as per rule 1 (travels up first)
            for j in i:
                if j > position:
                    floors_passed += abs(j - position)
                    position = j
                else:
                    floors_below.append(j)
            
            # then traverse floors below, from 
            for k in reversed(floors_below): # reverse this to be in order from highest bottom floor to least
                floors_passed += abs(k - position)
                position = k

        # Ouput results
        print("Total carlods:", total_carloads)
        print("  Total stops:", total_stops)
        print("Floors passed:", floors_passed)
        print("  Final floor:", position)


# MAIN FUNCTION

if __name__ == "__main__":
    # let's define some test cases
    test1 = [[3, 1, 4], [2, 8, 4], [4, 6, 4, 9]]


    # change these values to 
    elevator1 = Elevator(30, 5)

    elevator1.process_floors(test1)