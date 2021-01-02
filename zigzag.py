class Solution:
    def convert(self, s:str, numRows:int) -> str:
        if numRows == 1:
            return s
        length = len(s)
        l = ["" for _ in range(numRows)]
        for i in range(length):
            temp = self.zigzagList(numRows, length)
            l[temp[i]]+=(s[i])
        return ''.join(l)
    def zigzagList(self, n:int, length:int):
        l = []
        inv_l = []
        for i in range(n):
            l.append(i)
            inv_l.append(n-i-1)
        f = (l+inv_l[1:-1])*(int(length/(2*n-2))+1)
        return f[:length]

if __name__ == "__main__":
    sol = Solution()
    print(sol.convert("a", 1))