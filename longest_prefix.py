class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if len(strs) == 0:
            return ""
        else:
            for i in range(len(strs[0])):
                c = strs[0][i]
                for j in range(1, len(strs)):
                    if i==len(strs[j]) or strs[j][i] != c:
                        return strs[0][:i]
            return strs[0]
if __name__ == "__main__":
    s = Solution()
    print(s.longestCommonPrefix(["dog","racecar","car"]))