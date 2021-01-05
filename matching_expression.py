class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_transform = self.transform(s)
        if not(len(s_transform) == len(p)):
            return False
        for i in range(len(s_transform)):
            if not(s_transform[i]==p[i] or p[i]=='.'):
                return False
        return True

    def transform(self, s: str) -> str:
        # n = len(s)
        output = ""
        while len(s)>1:
            # current = s[0]
            output+= s[0]
            i=1
            while i<len(s) and s[i] == s[0]:
                i+=1
            if not(i==1):
                output+="*"
            s = s[i:]
        return output+s
        

if __name__ == "__main__":
    s = Solution()
    print(s.isMatch("ab", ".*"))