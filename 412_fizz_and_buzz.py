class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        return list(map(self.inner, range(1, n + 1)))
        
    def inner(self, n):
        three = n % 3 == 0
        five = n % 5 == 0
        res = ""
        
        if three:
            res += "Fizz"
        if five:
            res += "Buzz"
        if not res:
            res = str(n)
        
        return res


sol = Solution()
print(sol.fizzBuzz(15))

'''
hashing would have work too (but OrderedDict):

class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # ans list
        ans = []

        # Dictionary to store all fizzbuzz mappings
        fizz_buzz_dict = {3 : "Fizz", 5 : "Buzz"}

        for num in range(1,n+1):

            num_ans_str = ""

            for key in fizz_buzz_dict.keys():

                # If the num is divisible by key,
                # then add the corresponding string mapping to current num_ans_str
                if num % key == 0:
                    num_ans_str += fizz_buzz_dict[key]

            if not num_ans_str:
                num_ans_str = str(num)

            # Append the current answer str to the ans list
            ans.append(num_ans_str)  

        return ans

'''