"""
Write a function that implements binary search to find a target value in a sorted array. Return the index of the target if found, or -1 if not found.

Bonus: Print out the number of operations it took 
---
print(f"log₂{len(arr)} = {operations}")  
---
"""

def find_target(arr, target):
    # INSERT CODE HERE
    pass
    
def test(description, arr, target, expected):
    result = find_target(arr, target)
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
print("Running find_target tests:\n")

test("Basic case", [1, 3, 5, 7, 9], 5, 2)
test("Target not found", [1, 3, 5, 7, 9], 4, -1)
test("Empty array", [], 1, -1)
test("Single element", [5], 5, 0)
test("All same elements", [1,1,1,1,1], 1, 2)
test("Target at beginning", [1, 3, 5, 7, 9], 1, 0)
test("Target at end", [1, 3, 5, 7, 9], 9, 4)

