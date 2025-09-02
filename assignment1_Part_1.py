# assignment1_part1.py

class ListDivideException(Exception):
    pass

def list_divide(numbers, divide=2):
    """Return count of numbers divisible by 'divide'."""
    count = 0
    for num in numbers:
        if num % divide == 0:
            count += 1
    return count

def test_list_divide():
    """Run test cases and raise exception if any test fails."""
    if list_divide([1, 2, 3, 4, 5]) != 2:
        raise ListDivideException("Test 1 failed")
    if list_divide([2, 4, 6, 8, 10]) != 5:
        raise ListDivideException("Test 2 failed")
    if list_divide([30, 54, 63, 98, 100], divide=10) != 2:
        raise ListDivideException("Test 3 failed")
    if list_divide([]) != 0:
        raise ListDivideException("Test 4 failed")
    if list_divide([1, 2, 3, 4, 5], 1) != 5:
        raise ListDivideException("Test 5 failed")

# Run tests
test_list_divide()
print("All tests passed.")