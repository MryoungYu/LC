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
        max_len = 0
        max_start = -1
        for i in range(len(s)):
            left_cur_len = 0
            left_cur_start = -1
            left_flag = False

            right_cur_len = 0
            right_cur_start = -1
            right_flag = False

            for j in range(i/2 + 1):
                k = i - j
                l1 = len(s) - 1 - k
                l2 = len(s) - 1 - j
                # print(" i = %d, j = %d, k = %d, l1 = %d, l2 = %d" % (i,j,k, l1,l2))
                if ar[k][j] == '1':
                    if not left_flag:
                        left_flag = True
                        left_cur_start = j
                        left_cur_len += 1
                    else:
                        left_cur_len += 1
                else:
                    left_cur_start = -1
                    left_cur_len = 0
                    left_flag = False
                if ar[l1][l2] == '1':
                    if not right_flag:
                        right_flag = True
                        right_cur_start = l1
                        right_cur_len += 1
                    else:
                        right_cur_len += 1
                else:
                    right_cur_start = -1
                    right_cur_len = 0
                    right_flag = False
            left_real_cur_len = 0
            right_real_cur_len = 0
            if left_cur_len > 0:
                if i % 2 == 0:
                    left_real_cur_len = 2 * (left_cur_len - 1) + 1
                else:
                    left_real_cur_len = 2 * left_cur_len
            if right_cur_len > 0:
                if i % 2 == 0:
                    right_real_cur_len = 2 * (right_cur_len - 1) + 1
                else:
                    right_real_cur_len = 2 * right_cur_len
            if right_real_cur_len >= left_real_cur_len and right_real_cur_len > max_len:
                max_len = right_real_cur_len
                max_start = right_cur_start
            elif left_real_cur_len >= right_real_cur_len  and left_real_cur_len > max_len:
                max_len = left_real_cur_len
                max_start = left_cur_start
            # print("Left : i = %d, j = %d, cur_start = %d, cur_len = %d, real_cur_len = %d" % (i, j, left_cur_start, left_cur_len, left_real_cur_len))
            # print("Right : i = %d, j = %d, cur_start = %d, cur_len = %d, real_cur_len = %d" % (i, j, right_cur_start, right_cur_len, right_real_cur_len))

            
        # print("max_start = %d, max_len = %d" % (max_start, max_len))
        return s[max_start:max_start + max_len]







        # for i in range(len(s)):
        #     cur_len = len(s) - i
        #     for j in range(len(s) - cur_len + 1):
        #         # print('-----------------')
        #         sum = 0
        #         for k in range(cur_len):
        #             # print(j + k, j + cur_len - 1 - k, ar[j + k][j + cur_len - 1 - k])
        #             sum += int(ar[j + k][j + cur_len - 1 - k])
        #         if sum == cur_len:
        #             # print(j, cur_len, s[j:(j + cur_len)])
        #             return s[j:j + cur_len]
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
