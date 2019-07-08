from itertools import permutations 

'''
verrry clever:

def readBinaryWatch(self, num):
    mylist = []
    for i in range(12): 
        for j in range(60):
            if bin(i).count('1') + bin(j).count('1') == num:
                mylist.append('%d:%02d' %(i,j))
    return mylist

'''


class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        top_arr = [1, 2, 4, 8]
        bottom_arr = [1, 2, 4, 8, 16, 32]

        result = set()

        b = min(num, 6)
        t = num - b

        while b >= 0 and t <= 4:
            t_ = self.get_permutations(t, top_arr)
            b_ = self.get_permutations(b, bottom_arr)

            if len(t_) == 0:
                t_ = (0,)
            if len(b_) == 0:
                b_ = (0,)

            for pick_t in t_:
                for pick_b in b_:
                    if not isinstance(pick_t, tuple):
                        sum_t = pick_t
                    else:
                        sum_t = sum(pick_t)

                    if not isinstance(pick_b, tuple):
                        sum_b = pick_b
                    else:
                        sum_b = sum(pick_b)

                    if sum_t < 12 and sum_b < 60:
                        sum_b_str = str(sum_b)
                        result.add(str(sum_t) + ":" + (sum_b_str if len(sum_b_str) == 2 else "0" + sum_b_str))

            t += 1
            b -= 1
        
        return sorted(list(result))
    
    def get_permutations(self, num, arr):
        if num == 0:
            return []
        
        return list(permutations(arr, num))

sol = Solution()

res = sol.readBinaryWatch(1)
for item in res:
    print(item)