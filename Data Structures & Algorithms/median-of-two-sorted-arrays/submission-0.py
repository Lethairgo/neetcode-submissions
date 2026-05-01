class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        half = (len(nums1) + len(nums2)) // 2

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        left, right = 0, len(nums1) - 1
        
        while True:
            i = (left + right) // 2 # mid of nums1
            j = half - i - 2

            ALeft = nums1[i] if i >= 0 else float('-inf')
            ARight = nums1[i + 1] if (i + 1) < len(nums1) else float('inf')
            BLeft = nums2[j] if j >= 0 else float('-inf')
            BRight = nums2[j + 1] if (j + 1) < len(nums2) else float('inf')

            if ALeft <= BRight and BLeft <= ARight:
                if (len(nums1) + len(nums2)) % 2 == 0: # even
                    return (max(ALeft, BLeft) + min(ARight, BRight)) / 2
                else:
                    return min(ARight, BRight)
            elif ALeft > BRight:
                right = i - 1
            else:
                left = i + 1