#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Solution(object):
    """
    给你一个字符串 s，找到 s 中最长的回文子串。
    """
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ar = []
        for i in range(len(s)):
            ar.append([])
            for j in range(len(s)):
                if s[i] == s[j]:
                    ar[i].append('1')
                else:
                    ar[i].append('0')
        # for ar1 in ar:
            # print("\t".join(ar1))
        for i in range(len(s)):
            cur_len = len(s) - i
            for j in range(len(s) - cur_len + 1):
                # print('-----------------')
                sum = 0
                for k in range(cur_len):
                    # print(j + k, j + cur_len - 1 - k, ar[j + k][j + cur_len - 1 - k])
                    sum += int(ar[j + k][j + cur_len - 1 - k])
                if sum == cur_len:
                    # print(j, cur_len, s[j:(j + cur_len)])
                    return s[j:j + cur_len]
        # max_start = -1
        # max_len = 0
        # total_len = len(s)
        # for i in range(len(s)):
        #     l_start = -1
        #     l_cur_len = 0
        #     l_flag = False
        #     r_start = -1
        #     r_cur_len = 0
        #     r_flag = False
        #     for j in range(i + 1):
        #         # print(j, i - j, ar[j][i - j])
        #         if ar[j][i - j] == '1':
        #             if l_flag:
        #                 l_cur_len += 1
        #             else:
        #                 l_cur_len += 1
        #                 l_start = j
        #                 l_flag = True
        #         else:
        #             if l_cur_len > max_len:
        #                 max_len = l_cur_len
        #                 max_start = l_start
        #             l_cur_len = 0
        #             l_start = -1
        #             l_flag = False
        #         # print(total_len + j - i - 1, total_len - j - 1, ar[total_len + j - i - 1][total_len - j - 1])
        #         if ar[total_len + j - i - 1][total_len - j - 1] == '1':
        #             if r_flag:
        #                 r_cur_len += 1
        #             else:
        #                 r_cur_len += 1
        #                 r_start = total_len - j - 1
        #                 r_flag = True
        #         else:
        #             if r_cur_len > max_len:
        #                 max_len = r_cur_len
        #                 max_start = r_start - r_cur_len + 1
        #             r_cur_len = 0
        #             r_start = -1
        #             r_flag = False
        #     if l_cur_len > max_len:
        #         max_len = l_cur_len
        #         max_start = l_start
        #     if r_cur_len > max_len:
        #         max_len = r_cur_len
        #         max_start = r_start - r_cur_len + 1
        #     print(max_len, max_start)
        # return s[max_start:max_start + max_len]
        
        
        
        
    def longestPalindrome2(self, s):
        """
        :type s: str
        :rtype: str
        """
        if self.isPalindrome(s):
            return s
        else:
            s1 = self.longestPalindrome(s[1:])
            s2 = self.longestPalindrome(s[:-1])
            if len(s1) > len(s2):
                return s1
            else:
                return s2
        
    def isPalindrome(self, s):
        for i in range(len(s) / 2):
            if s[i] != s[len(s) - 1 - i]:
                return False
        return True


if __name__ == '__main__':
    obj = Solution()
    samples = [
        {
            'input': 'babad', 
            'output': 'bab'
        },
        {
            'input': 'cbbd', 
            'output': 'bb'
        },
        {
            'input': 'a',
            'output': 'a'
        },
        {
            'input': 'abb',
            'output': 'bb'
        },
        {
            'input': 'caba',
            'output': 'aba'
        },
        {
            'input': "aacabdkacaa",
            'output': 'aca'
        }
    ]
    for i in range(len(samples)):
        print("-----------------Case %d----------------" % i)
        s = samples[i]
        res = obj.longestPalindrome(s['input'])
        print("Input:")
        print(s['input'])
        print("My Output: ")
        print(res)
        print("Expect Output:")
        print(s['output'])
