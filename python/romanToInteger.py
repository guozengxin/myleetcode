# https://leetcode.com/problems/roman-to-integer/

class Solution(object):

    chars = {'I': (0, 1, 0),
            'V': (0, 5, 1),
            'X': (1, 1, 2),
            'L': (1, 5, 3),
            'C': (2, 1, 4),
            'D': (2, 5, 5),
            'M': (3, 1, 6)}

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        nums = [0, 0, 0, 0]
        preIndex = None
        for c in reversed(s):
            index = self.chars[c]
            if preIndex and preIndex[2] > index[2]:
                if preIndex[1] == 1:
                    nums[index[0]] = 9
                    nums[preIndex[0]] -= 1
                else:
                    nums[index[0]] = 4
            else:
                nums[index[0]] += index[1]
            preIndex = index
        result = 0
        times = 1
        for n in nums:
            result += n * times
            times *= 10
        return result

strs = ['I',
        'II',
        'VIII',
        'XIII',
        'XIX',
        'XLIX',
        'L',
        'LXIX',
        'CDXL',
        'LXXXVII',
        'MMXXXIV',
        ]

solu = Solution()
for s in strs:
    print s, solu.romanToInt(s)
