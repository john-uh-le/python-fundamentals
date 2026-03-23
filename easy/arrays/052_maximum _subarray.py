def maxSubArray(nums):
    """
    Return the maximum sum of a contiguous subarray within the given array.

    Time complexity: O(n), each element is processed once.
    Space complexity: O(1), no additional data structures are used.

    :type nums: List[int]
    :rtype: int
    """    
    max_sum = nums[0]
    current_sum = 0
    
    for i in range(len(nums)):
        current_sum += nums[i]
        max_sum = max(max_sum, current_sum)
        if current_sum < 0:
            current_sum = 0
    return max_sum

def maxSubArrayV2(nums):
    max_sum = nums[0]
    current_sum = 0

    start = 0
    end = 0
    temp_start = 0

    for i in range(len(nums)):
        current_sum += nums[i]

        # update best result
        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i

        # reset if negative
        if current_sum < 0:
            current_sum = 0
            temp_start = i + 1  # next index could be new start

    return max_sum, nums[start:end+1]

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  # 6
print(maxSubArray([1]))                      # 1
print(maxSubArray([5,4,-1,7,8]))            # 23
print(maxSubArray([-3,-2,-5]))              # -2

print(maxSubArrayV2([-2,1,-3,4,-1,2,1,-5,4]))  # 6
print(maxSubArrayV2([1]))                      # 1
print(maxSubArrayV2([5,4,-1,7,8]))            # 23
print(maxSubArrayV2([-3,-2,-5]))              # -2