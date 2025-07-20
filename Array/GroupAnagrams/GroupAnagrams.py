class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        g={}
      
        for i in strs:
            k=''.join(sorted(i))  """ join each sorted word from strs and make a sorted string"""
        
            if k not in g:    #Check if the k(shorted string) not in g ,Then create a new key:vaule pair with empty list 
                g[k]=[]

            g[k].append(i)  #update the empty list with value(unsorted word).
          
        return list(g.values())
