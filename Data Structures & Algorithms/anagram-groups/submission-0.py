class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l = []
        i = 0
        while (i<len(strs)):
            tl = [strs[i]]
            j = i+1
            while (j<len(strs)):
                if len(strs[j]) != len(strs[i]):
                    j+=1
                else:
                    w1 = strs[i]
                    w2 = strs[j]
                    d1 = {}
                    d2 = {}
                    for k in range(len(strs[i])):
                        if w1[k] not in (d1.keys()):
                            d1[w1[k]] = 1
                        else:
                            d1[w1[k]] += 1
                        if w2[k] not in (d2.keys()):
                            d2[w2[k]] = 1
                        else:
                            d2[w2[k]] += 1

                    if d1 == d2:
                        tl.append(w2)
                        strs.pop(j)
                    else:
                        j+=1
            l.append(tl)
            i+=1
        return l
                    
                