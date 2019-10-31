#-*- coding:utf-8 -*-
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if len(s) == 0 or numRows == 1:
            return s
        #声明一个numRows行的list
        ans_list = []
        tmp = 0
        while tmp < numRows:
            tmp_str = ''
            ans_list.append(tmp_str)
            tmp += 1

        #以 numRows+numsRows-2 个字符为一个循环
        circle = numRows + numRows - 2
        #遍历整个字符串，根据下标，决定将当前字符加入ans_list的哪一行
        index = 0
        line = 0
        real_index = 0
        while index < len(s):
            #将当前的index值映射到一个circle里面
            #real_index的取值范围为0 ~ circle-1
            real_index = index % circle
            if real_index < numRows:
                line = real_index
            else:
                line = circle - real_index
            ans_list[line] += s[index]
            #处理下一个字符
            index += 1
        
        #将numRows行的形式存放的最终结果，构造成字符串并返回
        ans = ''
        for it in ans_list:
            ans += it
        return ans

'''
functions for test
solution = Solution()
print(solution.convert('PAHNAPLSIIGYIR', 4))
'''