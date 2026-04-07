class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for s in strs:
            st = ''.join(sorted(s))
            if st in dic.keys():
                dic[st].append(s)
            else:
                dic[st] = [s]
        return list(dic.values())  
        
                    
                