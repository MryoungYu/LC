#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Solution(object):
    """
    Easy
    给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。

    回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

    例如，121 是回文，而 123 不是。
    
    提示：
        -231 <= x <= 231 - 1

    来源：力扣（LeetCode）
    链接：https://leetcode.cn/problems/palindrome-number
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        pass


if __name__ == '__main__':
    obj = Solution()
    samples = [
        {
            'input': [121], 
            'output': True
        },
        {
            'input': [-121], 
            'output': False
        },
        {
            'input': [10],
            'output': False
        }
    ]
    for i in range(len(samples)):
        print("-----------------Case %d----------------" % i)
        s = samples[i]
        res = obj.isPalindrome(s['input'][0])
        print("Input:")
        print(s['input'])
        print("My Output: ")
        print(res)
        print("Expect Output:")
        print(s['output'])
