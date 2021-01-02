class Solution:
    rev = 0
    def reverse(self, x: int) -> int:
        if x<0:
            negatif = True
            x = -x
        else:
            negatif = False

        while(x):    
            rest = x%10
            self.rev = self.rev*10 + rest
            x = x//10
        if abs(self.rev) > 2**31:
            return 0
        return -self.rev if negatif else self.rev
        

if __name__ == "__main__":
    s = Solution()
    print(s.reverse(-123456))