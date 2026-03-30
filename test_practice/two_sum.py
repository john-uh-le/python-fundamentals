def twoSum (self, nums : list[int], target : int) -> list[int]:
        """
        type: int
        type: int array
        rType: int
        """
        seen = {}

        for i , num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], i]
            seen[num] = i

        return None
    
print(twoSum([1,2,4,5,6,7,8], 9))
