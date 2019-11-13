# -*- coding:utf-8 -*-
class Solution:
    def threeSum(self, nums):
        tmp = sorted(nums)
        index = 0
        ans = set()
        while index < len(tmp):
            left = index + 1
            right = len(tmp) - 1
            target = 0 - tmp[index]
            while left < right:
                if tmp[left] + tmp[right] == target:
                    ans.add((tmp[index], tmp[left],tmp[right]))
                    left += 1
                    right -= 1
                elif tmp[left] + tmp[right] < target:
                    left += 1
                else:
                    right -= 1

            index += 1
        return ans

solution = Solution()
print(solution.threeSum([-1,0,1,2,-1,-4]))    