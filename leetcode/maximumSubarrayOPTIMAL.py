class Solution:
    def maxSubArray(self, nums):
        psum = [0]
        for x in nums:
            psum.append(psum[-1] + x)
        smallestNumberSeen = psum[0]
        ans = psum[1]
        psumNOTFIRST = psum[1:]
        for p in psumNOTFIRST:
            ans = max(ans, p-smallestNumberSeen)
            smallestNumberSeen = min(smallestNumberSeen, p)
        return ans
