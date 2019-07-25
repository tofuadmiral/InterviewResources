''' 
Practice interview 1

 Interviewer: Ray Liu
Practice for: Wealthsimple technical screen    
        Date: Friday July 12, 2019
'''

"""
We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

Example 1:
Input: 
asteroids = [5, 10, -5]
Output: [5, 10]
Explanation: 
The 10 and -5 collide resulting in 10.  The 5 and 10 never collide.
Example 2:
Input: 
asteroids = [8, -8]
Output: []
Explanation: 
The 8 and -8 collide exploding each other.
Example 3:
Input: 
asteroids = [10, 2, -5]
Output: [10]
Explanation: 
The 2 and -5 collide resulting in -5.  The 10 and -5 collide resulting in 10.
Example 4:
Input: 
asteroids = [-2, -1, 1, 2]
Output: [-2, -1, 1, 2]
Explanation: 
The -2 and -1 are moving left, while the 1 and 2 are moving right.
Asteroids moving the same direction never meet, so no asteroids will meet each other.
Note:

The length of asteroids will be at most 10000.
Each asteroid will be a non-zero integer in the range [-1000, 1000]..

"""



"""
[5, 10, -5]
    ^    ^
    left to right
        move again to right
        compare to right
        if collision, remove smaller one
        [5, 10]
        
    
    
    
    start at left most element
    
    check right, if it's gonna collide, compare sizes
        if collision, remove smaller, add larger to new array
    repeat on next element in array 
        if collision to right, remove smaller, add larger to new array
        if collision to left, remove smaller, update array 
        
    # hard for interviwer to follow we're were thinking
    seems like a messy coder
    half is about problem solving, and your thinking process
    organize your thoughts before you code anything
    
    make sure that the algorithm works before you code it, pseucode 
    
    add function definition when coding
    python snake casing:
        not camel case!!! just python convention 
        
    returnList -> return_list
    
    
    big takeaways
    * python conventions in naming
    * ptyhon datatypes
    * pseudocode first and consider cases
    * be more organized with thoughts so easier to translate into code
    * run through different testcases in your 
    * stack type questions: once you know it, it's all the same 
    
    Python data types
    * List - implements arrays and stacks 
    * Dictionary 
    * heapq
    * dequeue
    * graph (linkedlist, tree, other graphs)
    * define python classes (self notation)
    
    
    becme more familiar with python built in datatypes
        List
        Runtime and Space Complexity of each 
        
    
    #### how to actually pseudocode outline your cases 
    
    
    
    if left (neg) and right(positive)
        no collision
    elif left (pos) and right (neg)
        collion
    if left (neg) and right (neg)
        nothing 
    elif left (pos) and right (neg)
        nothing
    if first element is neg:
        nothing 
    

"""


asteroids = [5, 10, -5]
returnList = []

for i in range(len(asteroids)):
    
    # collision between left element and right element
    if asteroids[i] > 0 and asteroids[i+1] < 0 and i<len(asteroids)-1:
        if abs(asteroids[i]) == abs(asteroids[i+1]):
            continue
        returnList.add(max(abs(asteroids[i], abs(asteroids[i+1]))))
        
    # no collision, add to the stack
    
    # check what's currently in the stack 
    if returnList == []:
        returnList.add(asteroids[i])
    else:
        if returnList[-1] 
        
def collision(a: int, b: int) -> int:
    # collision between left element and right element
    if a > 0 and b < 0:
        if abs(asteroids[i]) == abs(asteroids[i+1]):
            return 0 
        else:
            return max(a, b)



    
      
        
    

