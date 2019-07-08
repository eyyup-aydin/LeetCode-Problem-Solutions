
import math

def isPowerOfThree(n):
    if n < 1:
        return False

    val = (math.log(n, 10) / math.log(3, 10))
    print('val ' + str(val) + '  int: ' + str(int(val)))
    return str(val)[-1] == '0'


'''
print(isPowerOfThree(1))
print(isPowerOfThree(2))
print(isPowerOfThree(9))
print(isPowerOfThree(27))
print(isPowerOfThree(45))
print(isPowerOfThree(25))
print(isPowerOfThree(49))
print(isPowerOfThree(81))
'''

print(isPowerOfThree(243))