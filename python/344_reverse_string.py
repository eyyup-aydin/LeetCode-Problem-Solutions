

def reverseString(s):
    """
    :type s: List[str]
    :rtype: None Do not return anything, modify s in-place instead.
    """

    f = 0
    l = len(s) - 1

    while l > f:
        temp = s[f]
        s[f] = s[l]
        s[l] = temp

        f += 1
        l -= 1
    
    print(s)


def reverseString2(s):
    length = len(s)

    for i in range(length // 2):
        s[i], s[length - i - 1] = s[length - i - 1], s[i]
    
    print(s)


reverseString(["a", "b", "c"])
reverseString(["a", "b", "c", "d"])
reverseString(["a"])
reverseString(["h","e","l","l","o"])