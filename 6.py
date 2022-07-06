#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Solution(object):
    """
    Medium
    将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。
    比如输入字符串为 "PAYPALISHIRING" 行数为 3 时，排列如下：

    P   A   H   N
    A P L S I I G
    Y   I   R
    之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："PAHNAPLSIIGYIR"。
    
    提示：
        1 <= s.length <= 1000
        s 由英文字母（小写和大写）、',' 和 '.' 组成
        1 <= numRows <= 1000

    来源：力扣（LeetCode）
    链接：https://leetcode.cn/problems/zigzag-conversion
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        ## Solution 1,试最笨的方法
        output = []
        for i in range(numRows):
            output.append([])
        line_no = 0
        forward = True
        for c in s:
            output[line_no].append(c)
            if forward:
                line_no += 1
                if line_no == numRows - 1:
                    forward = False
            else:
                line_no -= 1
                if line_no == 0:
                    forward = True
        output_str = ""
        for q in output:
            output_str += "".join(q)
        return output_str
        ## Solution 2. 直接算 index


if __name__ == '__main__':
    obj = Solution()
    samples = [
        {
            'input': ['PAYPALISHIRING', 3], 
            'output': 'PAHNAPLSIIGYIR'
        },
        {
            'input': ['PAYPALISHIRING', 4], 
            'output': 'PINALSIGYAHRPI'
        },
        {
            'input': ['A', 1],
            'output': 'A'
        }
    ]
    for i in range(len(samples)):
        print("-----------------Case %d----------------" % i)
        s = samples[i]
        res = obj.convert(s['input'][0], s['input'][1])
        print("Input:")
        print(s['input'])
        print("My Output: ")
        print(res)
        print("Expect Output:")
        print(s['output'])
