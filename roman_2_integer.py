# -*- coding:utf-8 -*-
class Solution:
    def judge(self, s, index):
        flag = True
        if index+1 < len(s):
            if s[index] == 'I' and s[index+1] == 'V':
                flag = False
            if s[index] == 'I' and s[index+1] == 'X':
                flag = False
            if s[index] == 'X' and s[index+1] == 'L':
                flag = False 
            if s[index] == 'X' and s[index+1] == 'C':
                flag = False
            if s[index] == 'C' and s[index+1] == 'D':
                flag = False
            if s[index] == 'C' and s[index+1] == 'M':
                flag = False
        return flag
    def romanToInt(self, s: str) -> int:
        answer = 0
        int_2_roman = {
            'I':1,'V':5,
            'X':10,'L':50,
            'C':100,'D':500,
            'M':1000
        }
        index = 0
        while index < len(s):
            current = int_2_roman[s[index]]
            if not self.judge(s, index):
                current *= -1
            answer += current
            index += 1
        return answer
'''
solution = Solution()
s = "MCMXCIV"
print(solution.romanToInt(s))
'''