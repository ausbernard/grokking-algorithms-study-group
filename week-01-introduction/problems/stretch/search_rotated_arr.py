"""
Given a sorted array that has been rotated at an unknown pivot, find a target value. Write a function that works in O(log n) time.

Bonus: Print out the number of operations it took 
---
print(f"log₂{len(arr)} = {operations}")  
---
"""
def search_rotated_arr(arr,target):
    # INSERT CODE HERE
    return -1

            

       
            
# Test 1: Basic case
assert search_rotated_arr([4,5,6,7,0,1,2], 0) == 4

# Test 2: Target not found
assert search_rotated_arr([4,5,6,7,0,1,2], 6) == -1

# Test 3: Empty array
assert search_rotated_arr([], 1) == -1

# Test 4: Two elements
assert search_rotated_arr([1,3], 3) == 1

# Test 5: Two elements
assert search_rotated_arr([3,1], 1) == 1


print("All tests passed!")
