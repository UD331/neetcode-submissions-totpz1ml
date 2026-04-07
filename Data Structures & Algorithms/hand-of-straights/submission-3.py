class Solution:
    def isNStraightHand(self ,hand, groupSize):
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)
        min_heap = list(count.keys())
        heapq.heapify(min_heap)  # O(n) heapify

        while min_heap:
            first = min_heap[0]  # smallest number in hand
            for i in range(first, first + groupSize):
                if count[i] == 0:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    # If this number has been exhausted, remove it from heap
                    if i != min_heap[0]:
                        return False  # must process in order
                    heapq.heappop(min_heap)
        
        return True