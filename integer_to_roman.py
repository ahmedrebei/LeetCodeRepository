class Solution:
    def intToRoman(self, num: int) -> str:
        thousands = num // 1000
        hundreds = (num % 1000) // 100
        tens = (num % 100) // 10
        units = num % 10
        thousands_list = ['', 'M', 'MM', 'MMM']
        hundreds_list = ['', 'C','CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
        tens_list = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
        units_list = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
        return thousands_list[thousands]+hundreds_list[hundreds]+tens_list[tens]+units_list[units]
        
if __name__ == "__main__":
    s = Solution()
    print(s.intToRoman(3999))