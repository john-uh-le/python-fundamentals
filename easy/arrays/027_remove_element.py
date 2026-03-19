def removeElement( nums, val):
        """
        remove an element from an array
        
        time complexity: o(n), you traverse the array only once
        space complexity: o(1), modification is in-place: no extra data used
        
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        write = 0
            
        for num in nums:
                if num != val:
                        nums[write] = num
                        write += 1
        return write
                
        
nums = [0,1,2,2,3,0,4,2]

k = removeElement(nums, 2)

print("k =", k)
print("result =", nums[:k])
print("altered list =", nums)
