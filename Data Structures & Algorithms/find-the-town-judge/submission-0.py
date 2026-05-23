class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        rel = defaultdict(set)
        for ai, bi in trust:
            rel[bi].add(ai)
        print(rel)
        for peo, tru in rel.items():
            if len(tru) == n-1:
                b = True
                for i in tru:
                    if peo in rel[i]:
                        b = False
                        break
                if b:
                    return peo
        
        return -1