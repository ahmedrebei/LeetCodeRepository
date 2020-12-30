class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        l = len(nums1) + len(nums2)
        if l%2:
            median_index = int(l/2)+1
            i = 0
            j = 0
            r = 0
            while (i+j+2<median_index):
                if nums1[i]>nums2[j]:
                    j+=1  
                    r = nums2[j]                  
                else:
                    i+=1
                    r = nums1[i]
            return r
        else:
            median_index = l/2
            i = 0
            j = 0
            r = 0
            while (i+j+2<median_index+1):
                r_prec = r
                if nums1[i]>nums2[j]:
                    j+=1  
                    r = nums2[j]                  
                else:
                    i+=1
                    r = nums1[i]
            return (r+r_prec)/2.0

if __name__ == "__main__":
    solution = Solution()
    nums1 = [1, 3, 15, 27]
    nums2 = [2, 9, 17, 21]
    solution.findMedianSortedArrays(nums1, nums2)