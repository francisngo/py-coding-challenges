from ast import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        currentSum = sum(nums[:k])
        maxSum = currentSum
        for i in range(len(nums) - k):
            currentSum = currentSum - nums[i] + nums[i + k]
            maxSum = max(maxSum, currentSum)

        return maxSum / k
