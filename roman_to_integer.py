class Solution:
    def romanToInt(self, s: str) -> int:        
        output = 0
        v = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1
        }
        for i in range(len(s)-1):
            if v[s[i+1]]>v[s[i]]:
                output -= v[s[i]]
            else:
                output += v[s[i]]
        return output + v[s[-1]]
if __name__ == "__main__":
    s = Solution()
    print(s.romanToInt("MCMXCIV"))        
