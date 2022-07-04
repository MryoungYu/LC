#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Solution(object):
    """
    Medium
    给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。

    如果反转后整数超过 32 位的有符号整数的范围 [−231,  231 − 1] ，就返回 0。

    假设环境不允许存储 64 位整数（有符号或无符号）。
    
    提示：
        -231 <= x <= 231 - 1

    来源：力扣（LeetCode）
    链接：https://leetcode.cn/problems/reverse-integer
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        pass


if __name__ == '__main__':
    obj = Solution()
    samples = [
        {
            'input': 123, 
            'output': 321
        },
        {
            'input': -123, 
            'output': -321
        },
        {
            'input':  120,
            'output': 21
        },
        {
            'input': 0,
            'output': 0
        }
    ]
    for i in range(len(samples)):
        print("-----------------Case %d----------------" % i)
        s = samples[i]
        res = obj.reverse(s['input'])
        print("Input:")
        print(s['input'])
        print("My Output: ")
        print(res)
        print("Expect Output:")
        print(s['output'])
