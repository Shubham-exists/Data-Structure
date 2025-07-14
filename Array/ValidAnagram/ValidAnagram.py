class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a={}
        if len(s) != len(t):
            return False
        
        for i in s:
            a[i] = a.get(i,0)+1

        '''for i in s:
                if i in a:
                    a[i] += 1
                else:
                    a[i] = 1'''

        for i in t:
            if i not in a or a[i] == 0:
                return False
            a[i] -=1
        
        return True
