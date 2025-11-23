"""
Given a sorted array with duplicates, find the starting and ending position of a target value. If not found, return [-1, -1]. Your algorithm must run in O(log n) time.

Bonus: Print out the number of operations it took 
---
print(f"log₂{len(arr)} = {operations}")  
---
"""
def first_last_position(arr,target):
    # INSERT CODE HERE
    return -1




def test(description, arr, target, expected):
    result = first_last_position(arr, target)
    try:
        assert result == expected, f"Expected {expected}, got {result}"
        print(f"PASS✅: {description}")
        return True
    except AssertionError as e:
        print(f"FAIL❌: {description}")
        print(f"    Input:  arr={arr}, target={target}")
        print(f"    {e}")
    
    return False
            
# Run tests
print("Running first_last_position tests:\n")

test("Basic case", [5,7,7,8,8,9], 8, [3,4])
test("Target not found", [1,2,3,4,5], 6, [-1,-1])
test("Empty array", [], 1, [-1,-1])
test("Single occurrence", [1,2,3,4,5], 3, [2,2])
test("All same elements", [1,1,1,1,1], 1, [0,4])