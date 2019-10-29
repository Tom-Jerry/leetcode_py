#-*- coding: utf-8 -*-
'''
题目要求：
给定两个有序数组nums1、nums2,这两者的长度分别为m、n。
要求出这两个有序数组的中位数

思路：
最简单的方法就是直接合并这两个数组，而后在合并生成的大数组中，
求中位数就可以。

points:
python2、python3做除法运算的机制不一样，
例如计算 5 / 2
python2会自动取整数，结果为2
python3会自动取小数，结果为2.5
'''
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        #合并这两个数组，并保持新生成的数组有序
        tmp = sorted(nums1 + nums2)
        answer = 0
        length = len(tmp)
        if length % 2 == 0:
            n1 = tmp[length // 2]
            n2 = tmp[(length // 2) - 1]
            tmp_answer = (float(n1) + float(n2)) / 2
        else:
            tmp_answer = tmp[length // 2]
        answer = float(tmp_answer)
        return answer
        
'''test the solution
solution = Solution()
result = solution.findMedianSortedArrays([1,3], [2,4])
print(result)
'''
