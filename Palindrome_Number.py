#-*- coding:utf-8 -*-
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        answer = True
        if not isinstance(x, int):
            return False
        elif x < 0:
            return False
        else:
            tmp_x = str(x)
            start = 0
            end = len(tmp_x) - 1
            while start < end:
                if tmp_x[start] != tmp_x[end]:
                    answer = False
                    break
                else:
                    start += 1
                    end -= 1
        return answer