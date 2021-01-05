class Solution:
    def threeSum(self, nums):
        output = []
        nums.sort()
        for i in range(len(nums)-1):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            a = nums[i]
            start = i + 1
            end = len(nums) - 1
            while (start<end):
                b = nums[start]
                c = nums[end]
                if (a + b + c == 0):
                    output.append([a, b, c])
                    start += 1
                    while start<end and nums[start] == nums[start-1]:
                        start += 1
                elif (a + b + c > 0):
                    end -= 1
                else:
                    start += 1
        return output

if __name__ == "__main__":
    s = Solution()
    print(s.threeSum([-1,0,1,2,-1,-4]))