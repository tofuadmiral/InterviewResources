'''
Coding Assignment: Elevator

 Author: Ahmed Fuad Ali
   Date: July 25, 2019
Version: 1.0.0


Summary: 

The following class models an elevator. This includes processing an input_arrayay of instructions, 
displaying it's final current_floor and actually peforming the required carloads. 

My approach was to convert every carload to a sorted unique list, 
and then iterate through each carload and perform the necessary operations to 
calculate floors passed, stops, and the current floor. I split the carload into
floors above and floors below, and traversed the floors above in order from
least to greatest, then traversed the floors below the current floor from greatest
to least, in order to simulate how an actual elevator works and keeping in mind Rule 1. 


Some Ambiguities:

Rule 1 Interpretation:
    I interpreted rule 1 to mean that if presented with the option of going either
    up or down, the elevator would move up FIRST and then move down.
    (i.e. if we're at 4 and the next carload is [3,5]
    then we'll move to the one up first and then the one down
    (in this example, move to 5 first and then move to 3)

    When moving down (i.e. if we're at 5 and the carload is [4,3])
    I assumed that the elevator would move to the nearest floors first, 
    as in moving first to 4 and then to 3, rather than moving to 3 and working 
    its way back up. This reduces floors passed and makes for a more efficient
    traversal of floors. 

No total floor count given for the building:
    I assumed that the given carloads would only have valid floors
    (i.e. no overflow past the top floor or underflow below the minimum)
    I think this is a valid assumption to make given that the carloads come from
    button presses within the elevator, which would only have valid floors. 
    For clarification, my algorithm does work with negative floors up to - MAX_INT
    and positive floors up to + MAX_INT, but assumes that all these are valid inputs. 


Complexity:
    Time complexity: O(n*logn), with n being the total number of floors in the array 
    of arrays (each floor in carload). This is due to the sorting of the carloads, which uses
    python's in built sorting function in n*logn time. everything else is done in linear time.

    Space complexity: The worst case space complexity is n, with n being the total number of floors
    in the array. This worst case arises because I initialize a new list of floors for "floors_below"
    and the worst case scenario is that the entire array is belowing the elevator's starting point. 

Errors:
    I noticed an issue with the test case. In the given example, the first carload is
    [3,1,4]. In the assignment document, it mentions that the car moves and delivers
    everyone at the correct floor, and the car is now on floor 4. This is incorrect. 
    The car starts at floor 5 (as stated in rule 4), moves to 4, then to 3, and finally
    to 1. Thus, the car should become empty and end up at floor 1, not 4. 

    The given example would have been correct if the elevator had started on floor 0, 
    in which case it would have traversed to 1, then to 3, and finally ended up at 4,
    however this contradicts rule 4 of the elevator starting on floor 5. 
'''


class Elevator:

    # initializer, specify the starting floor for each elevator
    def __init__(self, start):
        self.start = start
        

    # instance methods
    def process_floors(self, input_array):

        # initialize outputs
        total_carloads = len(input_array)
        total_stops = 0
        floors_passed = 0

        # keep track of what floor we're at 
        current_floor = self.start 

        # convert each carload to a set, then sort those sets
        # this removes duplicates and sorts from least to greatest 
        input_array = list(map(lambda x: sorted(list(set(x))), input_array))

        # for each carload, calculate stops and floors passed 
        for carload in input_array:
            floors_below = []
            total_stops += len(carload)

            # traverse floors above as per rule 1 (travels up first)
            for floor in carload:
                if floor > current_floor:
                    floors_passed += abs(floor - current_floor)
                    current_floor = floor
                else:
                    floors_below.append(floor)
            
            # traverse floors below
            for floor in reversed(floors_below): # reverse this to be in order from highest bottom floor to lowest
                floors_passed += abs(floor - current_floor)
                current_floor = floor

        # Ouput results
        print("Total carlods:", total_carloads)
        print("  Total stops:", total_stops)
        print("Floors passed:", floors_passed)
        print("  Final floor:", current_floor)
        print("--------------------")



# MAIN FUNCTION

if __name__ == "__main__":

    # test cases: 
    test1 = [[3, 1, 4], [2, 8, 4], [4, 6, 4, 9]]
    test2 = []
    test3 = [[1, 2, 2, 2, 2, 2], [3, 10, 50, 1], [6]]
    test4 = [[3, 1, 4], [2, 8, 4], [4, 6, 4, 9]]
    test5 = [[-3, 1, 4], [2, 8, -4], [4, 6, 4, -9]]




    elevator1 = Elevator(5)
    elevator1.process_floors(test1)
    elevator1.process_floors(test2)
    elevator1.process_floors(test3)
    elevator1.process_floors(test4)
    elevator1.process_floors(test5)
