#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Solution(object):
    """
    Hard
    给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。

    '.' 匹配任意单个字符
    '*' 匹配零个或多个前面的那一个元素
    所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。
    
    提示：
        1 <= s.length <= 20
        1 <= p.length <= 30
        s 只包含从 a-z 的小写字母。
        p 只包含从 a-z 的小写字母，以及字符 . 和 *。
        保证每次出现字符 * 时，前面都匹配到有效的字符

    来源：力扣（LeetCode）
    链接：https://leetcode.cn/problems/regular-expression-matching
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        pass


if __name__ == '__main__':
    obj = Solution()
    samples = [
        {
            'input': ['aa', 'a'], 
            'output': False
        },
        {
            'input': ['aa', 'a*'], 
            'output': True
        },
        {
            'input': ['ab', '.*'],
            'output': True
        }
    ]
    for i in range(len(samples)):
        print("-----------------Case %d----------------" % i)
        s = samples[i]
        res = obj.isPalindrome(s['input'][0], s['input'][1])
        print("Input:")
        print(s['input'])
        print("My Output: ")
        print(res)
        print("Expect Output:")
        print(s['output'])
