def find_max(nums):
    """
    Given a list of numbers, return the largest number in the list.

    Example

    [3,7,2,9,5]

    Output

    9
    """
    if len(nums) == 0:
        return None
    answer = nums[0]
    for num in nums[1:]:
        if answer < num:
            answer = num
    return answer

print( find_max([1,3,5,2,2,5,23]))