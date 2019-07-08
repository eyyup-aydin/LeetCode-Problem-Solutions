class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return '0'

        map = {
            10: 'a',
            11: 'b',
            12: 'c',
            13: 'd',
            14: 'e',
            15: 'f'
        }

        result = ""
        if num < 0:
            num = num + 2 ** 32
        while num > 0:
            rem = num % 16
            if rem < 10:
                result += str(rem)
            else:
                result += map[rem]

            num = num // 16

        return result[::-1]

sol = Solution()
res = sol.toHex(26)
print(res)

print()


'''
another:

def toHex(self, num: int) -> str:
    if num == 0:
        return '0'
    res = ''
    out = []
    if num < 0:
        num = num + 2**32
    
    while num > 0:
        res = num % 16
        if res >= 10:
            res -= 10
            out.insert(0, chr(ord('a') + res))
        else:
            out.insert(0, str(res))
        num //= 16
        
    return ''.join(out)

'''