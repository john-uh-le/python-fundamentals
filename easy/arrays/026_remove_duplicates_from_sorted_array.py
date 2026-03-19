def removeDuplicates(nums):
        """
        Remove duplicats from a sorted array in num
        
        time complexity: o(n) you have to read through 'nums' once to check for duplicates
        space complexity: o(1) only thing that is being made and updated is write and read. nums is being changed in place.
        
        
        :type nums: List[int]
        :rtype: int
        """
        
        # Check for non empty array
        if not nums:
            return 0
        
        
        write = 1
        
        # start at 1 becuase first item is unique
        for read in range(1, len(nums)):
            
            if nums[read] != nums[read -1]:
                
                nums[write] = nums[read]
                
                write += 1
            
        return write        
    
    
nums = [1, 1, 2, 2, 3]

k = removeDuplicates(nums)

print("k =", k)
print("result =", nums[:k])
    