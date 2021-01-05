class Solution:
    def maxArea(self, height) -> int:
        n = len(height)
        output = 0
        i=0
        j=n-1
        while(i<j):
            if height[i] < height[j]:
                output = max(output, (j-i)*height[i])
                i+=1
            else:
                output = max(output, (j-i)*height[j])
                j-=1
        return output
if __name__ == "__main__":
    s = Solution()
    print(s.maxArea([1,8,6,2,5,4,8,3,7]))