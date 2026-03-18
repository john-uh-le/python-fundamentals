"""
Given a list of numbers, return True if there are duplicates, otherwise return False.

Example:

[1,2,3,4] → False
[1,2,3,1] → True
"""
def contains_duplicates(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)

    return False

print("Test 1:", contains_duplicates([1,2,3,4,5]))

print(contains_duplicates([1,1,2,3,4,5]))

print(contains_duplicates([]))
