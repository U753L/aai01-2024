class Solution:
    def maxSubArray(self, nums):
        maxSum = nums[0]
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                maxSum = max(sum(nums[i:j+1]), maxSum)
        return maxSum
