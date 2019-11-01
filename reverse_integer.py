#-*- coding: utf-8 -*-
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        #在返回最终结果的时候，用flag变量来表明结果的正负
        flag = 1
        if x < 0:
            flag = -1
        #将x转换为绝对值，方便计算
        tmp_x = abs(x)
        ans = 0
        while tmp_x > 0:
            tmp = tmp_x % 10
            tmp_x = tmp_x // 10
            ans *= 10
            ans += tmp
        
        #处理非法输入数值
        if ans > 2147483647 or ans < -2147483648:
            return 0
        ans *= flag
        return ans