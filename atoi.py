class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MIN = -2**31 
        INT_MAX = 2**31 - 1
        l = len(s)
        i = 0
        output = 0
        negatif = False
        while(i<l and s[i] == ' '):
            i+=1
        s = s[i:]
        if len(s) == 0:
            return 0
        if s[0] in ['-','+']:
            negatif = s[0] == '-'
            s=s[1:]
        i=0
        l = len(s)
        while(i<l and s[i] in ['0','1','2','3','4','5','6','7','8','9']):
            output =  output*10 + int(s[i])
            i+=1
        if negatif:
            output = -output
        if output>INT_MAX:
            return INT_MAX
        if output < INT_MIN:
            return INT_MIN
        return output
        
if __name__ == "__main__":
    s = Solution()
    print(s.myAtoi("+42"))