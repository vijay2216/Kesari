class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if(len(nums) == 1):
            return 1
        else:
            if all(nums[i] <= nums[i+1] for i in range(len(nums) - 1)) or all(nums[i] >= nums[i+1] for i in range(len(nums) - 1)):
                return 1
            else:
                return 0
