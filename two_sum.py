#-*- coding:utf-8 -*-
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = []
        left = 0
        right = nums.__len__() - 1
        tmp = sorted(nums)
        while left < right:
            compare = tmp[left] + tmp[right]
            if compare < target:
                left += 1
            elif compare > target:
                right -= 1
            else: 
                res.append(left)
                res.append(right)
                break
                
        a = tmp[left]
        b = tmp[right]
        print(a, b)
        res = []
        index = 0
        for it in nums:
            if it == a or it == b:
                res.append(index)
            index += 1
        return res

solution = Solution()
res = solution.twoSum([3, 2, 4], 6)
print(res)