def find_duplicates(nums):
    """
    Return all duplicate numbers.

    [1,2,3,1,4,2]

    Output

    [1,2]
    """
    seen = set()
    duplicates = set()

    for num in nums:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)

    return list(duplicates)

