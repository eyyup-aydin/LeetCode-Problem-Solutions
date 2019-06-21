import math

def isPowerOfFour(num):
    """
    :type num: int
    :rtype: bool
    """
    if num < 1:
        return False

    val = math.log(num) / math.log(4)

    return str(val)[-1] == '0'


print(isPowerOfFour(0))
print(isPowerOfFour(1))
print(isPowerOfFour(4))
print(isPowerOfFour(16))
print(isPowerOfFour(64))
