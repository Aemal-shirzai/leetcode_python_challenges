RANGES = {
    range(1, 4): 'I', range(4, 5): 'IV',
    range(5, 9): 'V', range(9, 10): 'IX',
    range(10, 40): 'X', range(40, 50): 'XL',
    range(50, 90): 'L', range(90, 100): 'XC',
    range(100, 400): 'C', range(400, 500): 'CD',
    range(500, 900): 'D', range(900, 1000): 'CM', 
    range(1000, 4000): 'M',
}
class Solution:
    def intToRoman(self, num: int):
        result = ''
        remainder = num
        min_num, numeral = self.find_range(remainder)
        while True:
            result += numeral
            remainder -= min_num
            if remainder <= 0: return result
            min_num, numeral = self.find_range(remainder)

    def find_range(self, target_num):
        for key, val in RANGES.items():
            if target_num in key:
                min_num, numeral = min(key), val
                break
        return min_num, numeral