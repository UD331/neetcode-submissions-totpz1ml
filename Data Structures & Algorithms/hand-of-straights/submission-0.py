class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        while(hand):
            a = hand.pop(0)
            c = 1
            while (c<groupSize):
                if a+1 in hand:
                    a +=1
                    hand.remove(a)
                    c +=1
                elif c < groupSize:
                    return False
        return True