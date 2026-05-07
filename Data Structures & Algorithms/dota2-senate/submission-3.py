class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        c =i= 0
        senate = list(senate)
        while i < len(senate):
            if senate[i] == 'R':
                if c < 0:
                    senate.append('D')
                c+=1
            else:
                if c > 0:
                    senate.append('R')
                c-=1
            i+=1
        return 'Radiant' if c >0 else 'Dire'