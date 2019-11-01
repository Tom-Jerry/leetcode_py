#-*- coding:utf-8 -*-
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        start = 0
        str_num = ''
        flag = 1
        #find the first non-whitespace character
        while start < len(str) and str[start] == ' ':
            start += 1
        if start == len(str) or str[start].isalpha():
            return 0

        if str[start].isdigit():
            flag = 1 # for the value returned
        if str[start] == '+':
            if start < len(str)-1 and str[start+1].isdigit():
                flag = 1
                start += 1
            else:
                return 0
        if str[start] == '-':
            if start < len(str)-1 and str[start+1].isdigit():
                flag = -1
                start += 1
            else:
                return 0
        
        #find the end of number-sequeences 
        while start < len(str) and str[start].isdigit():
            str_num += str[start]
            start += 1

        # atoi
        ans = 0
        for s in str_num:
            ans *= 10
            ans += int(s)
        ans *= flag

        #deal with overflow
        INT_MAX = pow(2, 31) - 1
        INT_MIN = -pow(2, 31)
        if ans > INT_MAX:
            return INT_MAX
        if ans < INT_MIN:
            return INT_MIN
        return ans


'''
'''
solution = Solution()
res = solution.myAtoi('     -42')
print(res)