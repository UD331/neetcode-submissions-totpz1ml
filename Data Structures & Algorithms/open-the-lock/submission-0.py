class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if target == '0000':
            return 0
        visit = set(deadends)
        if '0000' in visit:
            return -1
        q = deque(['0000'])
        visit.add('0000')
        steps = 0

        while q:
            steps+=1
            for _ in range(len(q)):
                lock = q.popleft()
                for i in range(4):
                    for j in [-1,1]:
                        digit = str((int(lock[i]) + j + 10)%10)
                        next_lock = lock[:i]+digit+lock[i+1:]
                        if next_lock in visit:
                            continue
                        if next_lock == target:
                            return steps
                        q.append(next_lock)
                        visit.add(next_lock)
        return -1