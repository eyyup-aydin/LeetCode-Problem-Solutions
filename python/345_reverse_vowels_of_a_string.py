class Solution(object):
    VOWELS = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]
    
    def reverseVowels(self, s):
        input = list(s)
        if len(input) < 2:
            return s

        left = 0
        right = len(input) - 1

        while left < right:
            leftBool = input[left] in self.VOWELS
            rightBool = input[right] in self.VOWELS
            if leftBool and rightBool:
                input[left], input[right] = input[right], input[left]
                left += 1
                right -= 1
            elif not leftBool and not rightBool:
                left += 1
                right -= 1
            elif leftBool:
                right -= 1
            else:
                left += 1

        return ''.join(input)
         