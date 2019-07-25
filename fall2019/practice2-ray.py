"""

Question:

Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.


"""



"""
Fuad's Notes

[[1,3],[2,6],[8,10],[15,18]]



[[1,3],[2,6],[8,10],[15,18], [4, 5]]


[[1,3],[2,6],[8,10], [11, 20], [15,18]]
    
    


[1,6], [8, 10], 

    
    stack 
    
    
    [1, 6], [8, 10], [15,18], 
    
    
    
    
    [[1,3],[2,6],[8,10],[15,18]]

    
    
    
    cases:
    
    1: they merge
        update our stack with merged range
        
    2: they don't merge:
        update our stack with new interval    
"""


"""
    [[1,3],[2,6],[8,10],[15,18]]
    
    stack: [1,6], [8, 10], [15,18]
    
    
    
        intervals = intervals.sort(key = lambda x: x[0])
        
            look up how to use the sort
            
            minor errors in coding i.e. return statement and elif vs if, 
            no need to check things twice
"""
            
def merge_intervals(intervals):
    intervals = intervals.sort(key = lambda x: x[0])
    
    stack = []
    
    for i in intervals:
        if stack == []:
            stack.append(i)
        elif i[0] <= stack[-1][1]:
            stack[-1] = [stack[-1][0], max(stack[-1][1], i[1])]
        else:
            stack.append(i)
            
    return stack
        

"""
QUESTION 2

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:

Input: [3,4,5,1,2] [3,4,5,1,2] 
Output: 1
Example 2:

Input: [4,5,6,7,0,1,2]
Output: 0

    [4,5,6,7,0,1,2]
    
    [0, 1, 2]
    
    [0], [2]
    
    
    

        [99, 100, 101, 96, 97, 98] 
        
        Input: [3,4,5,1,2] 
    
    
        [4,5,6,7,0,1,2]
        
        [3] [3]
        
        [1] [1]
        
        
        [1, 2, 3, 4]    
        
        
        
        cases:
        
        middle < left
            pivot point is on the left side
            check the left sublist
            check if preceeding is greater than our element
            
        middle > left
            pivot is on the right
            check the right sublist
            check if preceeding is greater than our element 
            
        
        
                [4,5,6,7,0,1,2]

        
"""


array = [-1,2,3,4,5]

def find_minimum (array):
    
    left = 0
    right = len(array)-1
    middle = right//2 
    
    if array == []:
        return 0
    
    if array[0] < array[-1]:
        return array[0]
    
    
    while left <= middle:
        if array[middle] < array[middle-1]:
            return array[middle]
        elif array[middle] < array[left]:
            right = middle
            middle = (right + left) // 2
        elif array[middle] > array[left]:
            left = middle
            middle = (right + left) // 2
        


print(find_minimum(array))





