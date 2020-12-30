class DynamicProgrammingSolution:
    """
    The idea is utilize to fact that is s is plindrome 
    removing the first and the last caracter will reserve 
    the proprety
    i.e:
    s = "ahjjha" is palindrome, so is "hjjh"
    First, strings with length one or length two with similar caracters
    are palindrome.
    Then, we check the rest of the given string by adding caracters from both side
    """
    def longestPalindrome(self, s: str) -> str:
        l = len(s)
        if l in [1, 2]:
            return s if s[0]==s[-1] else s[0]
        
        p = [[False for _ in range(l)] for _ in range(l)]
        # diagonal elements represent string with one caracter
        # checking for length two string with the same caracter
        index, m = 0, 1
        for i in range(l-1):
            p[i][i] = True
            if s[i] == s [i+1]:
                p[i][i+1] = True
                m = 2
                index = i
        p[-1][-1] = True

        
        for k in range(3, l+1):
            for i in range(l-k+1):
                if p[i+1][i+k-2] and s[i]==s[i+k-1]:
                    p[i][i+k-1] = True
                    m = k
                    index = i
        return s[index:index+m]


        
        

if __name__ == "__main__":
    sol = DynamicProgrammingSolution()
    s = "ccc"
    print(sol.longestPalindrome(s))
