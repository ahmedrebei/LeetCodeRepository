class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        i=0
        m = 0
        hashMap = dict()
        for j in range(n):
            if s[j] in hashMap:
                i = max(i, hashMap[s[j]]+1)
            
            m = max(m, j-i+1)
            hashMap[s[j]] = j
        return m


if __name__ == "__main__":
    solution = Solution()
    s = "abcdeafbdgcbb"
    print(solution.lengthOfLongestSubstring(s))
