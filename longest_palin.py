class Solution(object):

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        #当输入的字符串为空、输入的字符串只由一个字符组成的时候
        #直接返回原始字符串即可
        if s == '' or len(set(list(s))) == 1:
            return s

        answer = ''     #记录最终答案
        begin = 0
        maxlen = 1
        center = 0      #每次从下标为center的位置开始，寻找当前位置的最长回文子串
        while center < len(s):
            l = center
            r = center
            #若同一个字符连续出现，使右边界越过重复部分
            while (r < len(s)-1) and (s[r] == s[r+1]):
                r = r + 1
            center = r + 1
            #以当前center位置为中心，向左右两个方向展开，求出此时最长回文子串的长度以及始、终位置
            #这里需要注意的是，先判断左右两边将要去的位置上的字符相等（先判断能不能去），再向两边移动
            #为了保证判断的时候，数组下标不越界，判断l和r的临界条件时候i不能加等号
            while (l > 0) and (r < len(s)-1) and s[l-1] == s[r+1]:
                l = l - 1
                r = r + 1
            if maxlen < r - l + 1:
                maxlen = r - l + 1
                begin = l
        return s[begin:begin+maxlen]        
        