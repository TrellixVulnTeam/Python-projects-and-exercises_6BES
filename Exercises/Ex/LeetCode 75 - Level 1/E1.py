
# 1480. Running Sum of 1d Array

# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

nums = [1, 2, 3, 4]


def runningSum(List):

    for i in range(1, len(nums)):
        nums[i] += nums[i-1]

    return nums


print(runningSum(nums))
