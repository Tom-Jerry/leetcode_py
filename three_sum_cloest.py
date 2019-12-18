#-*- coding:utf-8 -*-
class Solution:
    def threeSumClosest(self, nums,target):
        if not nums:
            return None
        nums.sort()
        diff = float('inf')
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if (abs(sum-target) < diff):
                    diff = abs(sum-target)
                    output = sum
                if sum < target:
                    left += 1
                elif sum > target:
                    right -= 1
                else:
                    return target
        return output 

solution = Solution()
print(solution.threeSumClosest([0,2,1,-3], 1))
        