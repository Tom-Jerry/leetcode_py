# -*- coding:utf-8 -*-
class Solution:
    def judge(self, flag, loc, strs):
        index = 1
        result = True
        while index < len(strs):
            if flag != strs[index][loc]:
                result = False
            index += 1
        return result

    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""

        prefix = ""

        min_len = len(strs[0])
        for s in strs:
            min_len = min(min_len, len(s))

        location = 0
        flag = ""
        while location < min_len:
            flag = strs[0][location]
            if self.judge(flag, location, strs):
                prefix += flag
            else:
                break
            location += 1
        
        return prefix
               
solution = Solution()
print(solution.longestCommonPrefix(["aca","cba"]))

