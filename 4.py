class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        total_len = len(nums1) + len(nums2)
        if total_len % 2 == 0:
            target_index = [total_len / 2, (total_len / 2) + 1]
        else:
            target_index = [(total_len + 1) / 2]
        
        index = 0
        nums3 = []
        sum = 0
        i = 0
        j = 0
        while i < len(nums1) or j < len(nums2):
            if i < len(nums1) and j < len(nums2):
                if nums1[i] <= nums2[j]:
                    cur = nums1[i]
                    i += 1
                    index += 1
                else:
                    cur = nums2[j]
                    j += 1
                    index += 1
            elif i < len(nums1):
                cur = nums1[i]
                i += 1
                index += 1
            elif j < len(nums2):
                cur = nums2[j]
                j += 1
                index += 1
            else:
                break
            if index in target_index:
                nums3.append(cur)
                sum += cur
                if len(target_index) == len(nums3):
                    break
        return float(sum) / len(target_index)
                    
if __name__ == '__main__':
    obj = Solution()
    samples = [
        {'input':[[1, 3], [2]], 'output': 2.0},
        {'input': [[1, 2], [3, 4]], 'output': 2.5}
    ]
    for i in range(len(samples)):
        s = samples[i]
        res = obj.findMedianSortedArrays(s['input'][0], s['input'][1])
        print("Case %d:" % i)
        print("My Output: ")
        print(res)
        print("Expect Output:")
        print(s['output'])