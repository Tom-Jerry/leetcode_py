#-*- coding:utf-8 -*-
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        #输入的字符串为空,进行排错处理
        if s.__len__() == 0:
            return 0

        visited = ""    #记录从当前起点找到的，不包含重复字符的最长子串
        res_max = 0
        for c in s:
            if c not in visited:
                visited += c
            else:
                visited = visited[(visited.index(c)+1):] + c
            res_max = max(res_max, visited.__len__())

        return res_max