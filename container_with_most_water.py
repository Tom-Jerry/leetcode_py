# -*- coding: utf-8 -*-
'''
#此法可以求解，但是在处理超大规模输入的时候会超过时间限制
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ans = 0
        distance = len(height) - 1
        while distance > 0:
            start = 0
            end = start + distance
            while end < len(height):
                tmp = distance * (min(height[start], height[end]))
                ans = max(ans, tmp)
                start += 1
                end += 1
            distance -= 1
        return ans
'''
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ans = 0
        start = 0
        end = len(height) - 1
        while start < end:
            ans = max(ans, min(height[start], height[end])*(end-start))
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        return ans
'''test area
solution = Solution()
into = [9,6,14,11,2,2,4,9,3,8]
result = solution.maxArea(into)
print(result)
'''