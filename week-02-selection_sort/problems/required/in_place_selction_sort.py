"""
Modify selection sort to work in-place without creating a new array, by swapping elements. If no array, return -1
"""

def in_place_selection_sort(arr):
    # Insert your code here
    return -1

def test(description, arr, expected):
    result = in_place_selection_sort(arr)
    try:
        assert result == expected, f"Expected {expected}, got {result}"
        print(f"PASS✅: {description}")
        return True
    except AssertionError as e:
        print(f"FAIL❌: {description}")
        print(f"    Input:  arr={arr}")
        print(f"    {e}")
    
    return False
            
# Run tests
print("Running first_last_position tests:\n")

test("Base Case", [2,1,5,4,3], [1,2,3,4,5])
test("Duplicates", [7,5,7,8,2,9], [2,5,7,7,8,9])
test("Multiple Duplicates", [7,5,7,8,2,9], [2,5,7,7,8,9])
test("Already Sorted", [1,2,3,4,5], [1,2,3,4,5])
test("Empty array", [], -1)
test("All same elements", [1,1,1,1,1], [1,1,1,1,1])