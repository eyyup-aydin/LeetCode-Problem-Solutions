class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        
        ransomNote = list(ransomNote)
        magazine = list(magazine)

        for char in ransomNote:
            if char in magazine:
                magazine.remove(char)
            else:
                return False
        
        return True

sol = Solution()
print(sol.canConstruct("a", "b"))
print(sol.canConstruct("aa", "ab"))
print(sol.canConstruct("aa", "aab"))


'''
other solutions:

dic = {}
for s in ransomNote:
    dic[s] = ransomNote.count(s)
for key in dic.keys():
    if magazine.count(key) < dic[key]:
        return False
return True

----------
ransomCounter = collections.Counter(ransomNote)
        magCounter = collections.Counter(magazine)
        for c,v in ransomCounter.items():
          if v > magCounter[c]:
            return False
        return True
------

def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if (len(ransomNote) > len(magazine)):
            return False
        
        for note in ransomNote:
            try:
                index = magazine.index(note)
                magazine = magazine[:index] + magazine[index+1:]
            except:
                return False
            
        return True

'''